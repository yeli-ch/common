
"""Configure your app with a config file with the option to override it via
command line arguments"""

import argparse
import configparser
import sys
import os.path


class Config:
    """Reads configs from the command line and config files"""

    def __init__(self, app_name, description, configs):
        """Read configs from the command line and configs files."""

        # First, parse only the command line argument that specifies the config file
        # Don't show the help yet because we haven't added all possible arguments yet
        arg_parser = argparse.ArgumentParser(description = description, add_help = False)
        arg_parser.add_argument("-c,--config",
                                action = "store",
                                dest = "config",
                                help = "Specify a configuration file")

        # Ignore any additional unknown arguments
        args, remaining = arg_parser.parse_known_args()

        # Fall back to the default global config file if none was specified
        if args.config:
            config_file = args.config
        else:
            config_file = "/etc/yeli.conf"

        # Check whether the config file exists
        file_args = {}
        if not os.path.isfile(config_file):
            # It's not yet fatal if it doesn't exist, if the user still gives all arguments
            # everything is fine
            print("Warning: Config file '{0}' does not exist.".format(config_file))
        else:
            # Now read the defaults from the appropriate config file
            file_parser = configparser.ConfigParser()
            file_parser.read(config_file)
            try:
                file_args = file_parser[app_name]
            except KeyError:
                print("Error: Config file is missing a '{0}' section.".format(app_name), file = sys.stderr)
                sys.exit(22)

        # Now add the remaining configs with the appropriate defaults from the config file
        arg_parser = argparse.ArgumentParser(parents = [arg_parser])
        for conf in configs:
            conf_name = conf['long'][2:]  # Strip the '--'
            if conf['short']:
                arg = "{0},{1}".format(conf['short'], conf['long'])
            else:
                arg = conf['long']
            # Set the default based on what we read from the config file
            default = file_args.get(conf_name, None)
            if default:
                required = False
            else:
                required = True
            action = conf['action']
            if action == "store_true" or action == "store_false":
                # We need to convert the string for store_true/false first
                if default and default.lower() == "true":
                    default = True
                elif default and default.lower() == "false":
                    default = False
                else:
                    default = bool(action == "store_false")

                arg_parser.add_argument(arg,
                                        action = "store_true",
                                        dest = conf_name,
                                        help = conf['help'],
                                        default = default)
            else:
                arg_parser.add_argument(arg,
                                        action = conf['action'],
                                        type = conf['type'],
                                        dest = conf_name,
                                        help = conf['help'],
                                        default = default,
                                        required = required)

        # Finally, parse the remaining command line arguments and populate
        # the dict (self) with the values
        final_args = arg_parser.parse_args(remaining)
        self.__dict__.update(final_args.__dict__)


import argparse
import configparser
from sys import exit


class Config(dict):
    """Reads configs from the command line and config files"""

    def __init__(self, app_name, description, configs):
        """Read configs from the command line and configs files."""

        super(Config, self).__init__()












        # Parse command line arguments first
        parser = argparse.ArgumentParser(description = description)
        parser.add_argument("-c,--config",
                                type = argparse.FileType('r'),
                                action = "store",
                                dest = "config",
                                help = "Specify a configuration file")
        for conf in configs:
            arg = conf['long']
            if conf['short'] is not None:
                arg = "{0},{1}".format(arg, conf['short'])
            parser.add_argument(arg,
                                action = conf['action'],
                                type = conf['type'],
                                dest = conf['long'],
                                help = conf['help'])
        cmdline_args = parser.parse_args()

        # Now parse the appropriate config file
        if cmdline_args['config'] is not None:
            file = cmdline_args['config']
        else:
            file = "/etc/yeli/" + app_name
        parser = configparser.ConfigParser()
        parser.read(file)
        try:
            file_args = parser['DEFAULT']
        except KeyError:
            print("Error: Config file is missing 'DEFAULT' section.")
            exit(22)

        # Fill the arguments that were not supplied via command line
        # with the ones from the config file
        for name, arg in cmdline_args.items():
            if arg is None:
                try:
                    if configs
                    self[name] = file_args[name]
                except KeyError:
                    print("Error: Config missing: " + name)
                    exit(22)
            else:
                self[name] = arg

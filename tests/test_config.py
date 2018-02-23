
import unittest
import sys
from unittest.mock import patch


class ConfigTest(unittest.TestCase):

    def tearDown(self):
        try:
            del sys.modules['context']
        except KeyError:
            pass

    def test_valid_global_file_only(self):
        pass

    def test_valid_local_file_only(self):
        configs = [
            {
                "short": "-a",
                "long": "--first",
                "action": "store",
                "type": str,
                "help": "Fist argument"
            },
            {
                "short": "-b",
                "long": "--second",
                "action": "store_true",
                "help": "Second argument"
            }
        ]
        testargs = ["prog", "-c", "config.conf"]
        with patch.object(sys, 'argv', testargs):
            from context import Config
            conf = Config("Test", "Just a test", configs)
            self.assertEqual(conf.first, "a")
            self.assertTrue(conf.second)

    def test_valid_cmdline_args_only(self):
        configs = [
            {
                "short": "-a",
                "long": "--first",
                "action": "store",
                "type": str,
                "help": "Fist argument"
            },
            {
                "short": "-b",
                "long": "--second",
                "action": "store_true",
                "help": "Second argument"
            }
        ]
        testargs = ["prog", "-a", "something"]
        with patch.object(sys, 'argv', testargs):
            from context import Config
            conf = Config("Test", "Just a test", configs)
            self.assertEqual(conf.first, "something")
            self.assertFalse(conf.second)

    def test_valid_global_and_local_file(self):
        pass

    def test_valid_local_and_cmdline_no_overwrite(self):
        pass

    def test_valid_local_and_cmdline_overwrite(self):
        pass

    def test_invalid_global_file_only(self):
        pass

    def test_invalid_local_file_only(self):
        pass

    def test_invalid_cmdline_args_only(self):
        pass

    def test_valid_local_file_invalid_cmdline_args_no_overwrite(self):
        pass

    def test_valid_local_file_invalid_cmdline_args_overwrite(self):
        pass

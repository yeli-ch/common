
import unittest
from config import Config
from mock import patch


class ConfigTest(unittest.TestCase):

    def test_valid_global_file_only(self):
        pass

    def test_valid_local_file_only(self):
        configs = {
            {
                "short": "-a",
                "long": "--first",
                "action": "store",
                "help": "Fist argument"
            },
            {
                "short": "-b",
                "long": "--second",
                "action": "store_true",
                "help": "Second argument"
            }
        }
        conf = Config("TEST", "Just a test", configs)
        self.assertEqual(conf['first'], "a")
        self.assertEqual(conf['second'], "b")

    def test_valid_cmdline_args_only(self):
        testargs = ["prog", "-a", "first"]
        with patch.object(sys, 'argv', testargs)

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

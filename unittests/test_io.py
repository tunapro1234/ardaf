import ardaf.lib.IO_functions as io
import ardaf.res.glob as glob
import unittest
import json
import os


class TestIO(unittest.TestCase):
    def setUp(self):
        self.json_path = "ardaf/test/profile.json"

        try:
            os.remove(self.json_path)
        except FileNotFoundError:
            pass

        except:
            raise Exception("wtf")

        with open(self.json_path, "w+") as file:
            json.dump(io.encrypt(glob.default_profile), self.json_path)

    def tearDown(self):
        try:
            os.remove(self.json_path)
        except FileNotFoundError:
            pass

    def test_get_settings(self):
        self.assertEqual(glob.default_profile,
                         io.get_settings(path=self.json_path))

    def test_save_settings(self):
        with open(self.json_path, "w+") as file:
            file.write("")

        result = io.save_settings(glob.default_profile, self.json_path)
        
        self.assertEqual(result, True)
        self.assertEqual(glob.default_profile,
                         io.decrypt(json.load(self.json_path)))

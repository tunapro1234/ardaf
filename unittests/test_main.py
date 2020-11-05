import ardaf as package
import unittest


class TestMain(unittest.TestCase):
    def test_main(self):
        correct_result = None
        result = package.main()

        self.assertEqual(result, correct_result)
from unittest import TestCase, main
import os

from searching.medium_problems.pairs.pairs_brute_force import pairs_brute_force
from test_utilities.time_complexity_file_processing_functions import get_console_time_logged_result_of
from test_utilities.time_complexity_file_processing_functions import process_test_file_where_single_line_is_an_int_array

current_path = os.path.dirname(__file__)
test_resources_path = current_path + "/test_resources/"


class BruteForcePairsTester(TestCase):

    functionality_test_data: dict = {
        "test_0": {
            "k": 2,
            "arr": [1, 5, 3, 4, 2],
            "expected": 3
        },
        "test_1": {
            "k": 1,
            "arr": [
                363374326,
                364147530,
                61825163,
                1073065718,
                1281246024,
                1399469912,
                428047635,
                491595254,
                879792181,
                1069262793
            ],
            "expected": 0
        },
        "test_2": {
            "k": 2,
            "arr": [1, 3, 5, 8, 6, 4, 2],
            "expected": 5
        },
    }

    def test_functionality_0(self):
        test_data = self.get_functionality_test_data("test_0")
        k: int = test_data["k"]
        arr: list = test_data["arr"]

        expected: int = test_data["expected"]
        actual: int = pairs_brute_force(k, arr)
        self.assertEqual(expected, actual)

    def test_functionality_1(self):
        test_data = self.get_functionality_test_data("test_1")
        k: int = test_data["k"]
        arr: list = test_data["arr"]

        expected: int = test_data["expected"]
        actual: int = pairs_brute_force(k, arr)
        self.assertEqual(expected, actual)

    def test_functionality_2(self):
        test_data = self.get_functionality_test_data("test_2")
        k: int = test_data["k"]
        arr: list = test_data["arr"]

        expected: int = test_data["expected"]
        actual: int = pairs_brute_force(k, arr)
        self.assertEqual(expected, actual)

    def get_functionality_test_data(self, test_name: str) -> dict:
        functionality_test_data: dict = self.functionality_test_data[test_name]
        return functionality_test_data


if __name__ == "__main__":
    main()



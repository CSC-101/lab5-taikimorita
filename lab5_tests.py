import data
import lab5
import unittest


# Write your test cases for each part below.

class TestCases(unittest.TestCase):
    # Part 1
    #    Part 1 tests should be in data_tests.py.

    # Part 2
    #    Part 2 tests should be in data_tests.py.

    # Part 3
    def test_time_add_no_overflow(self):
        time1 = data.Time(2, 30, 15)
        time2 = data.Time(1, 20, 10)
        result = lab5.time_add(time1, time2)
        expected = data.Time(3, 50, 25)
        self.assertEqual(result, expected)

    def test_time_add_with_seconds_overflow(self):
        time1 = data.Time(2, 30, 45)
        time2 = data.Time(1, 20, 30)
        result = lab5.time_add(time1, time2)
        expected = data.Time(3, 51, 15)
        self.assertEqual(result, expected)

    def test_time_add_with_minutes_overflow(self):
        time1 = data.Time(2, 45, 30)
        time2 = data.Time(1, 20, 40)
        result = lab5.time_add(time1, time2)
        expected = data.Time(4, 6, 10)
        self.assertEqual(result, expected)

    # Part 4
    def test_is_descending_true(self):
        self.assertTrue(lab5.is_descending([5.0, 4.0, 3.0, 2.0, 1.0]))

    def test_is_descending_false(self):
        self.assertFalse(lab5.is_descending([5.0, 3.0, 4.0, 2.0, 1.0]))

    def test_is_descending_equal_elements(self):
        self.assertFalse(lab5.is_descending([5.0, 5.0, 5.0]))

    def test_is_descending_empty_list(self):
        self.assertTrue(lab5.is_descending([]))

    def test_is_descending_single_element(self):
        self.assertTrue(lab5.is_descending([3.0]))

    # Part 5
    def test_largest_between_valid_range(self):
        nums = [1, 3, 5, 2, 4]
        result = lab5.largest_between(nums, 1, 4)
        expected_index = 2
        self.assertEqual(result, expected_index)

    def test_largest_between_invalid_range(self):
        nums = [1, 3, 5, 2, 4]
        result = lab5.largest_between(nums, 4, 1)
        self.assertIsNone(result)

    def test_largest_between_out_of_bounds(self):
        nums = [1, 3, 5, 2, 4]
        result = lab5.largest_between(nums, -1, 10)
        expected_index = 2
        self.assertEqual(result, expected_index)

    def test_largest_between_single_element(self):
        nums = [7]
        result = lab5.largest_between(nums, 0, 0)
        expected_index = 0
        self.assertEqual(result, expected_index)

    def test_largest_between_empty_list(self):
        nums = []
        result = lab5.largest_between(nums, 0, 0)
        self.assertIsNone(result)

    # Part 6
    def test_furthest_from_origin_valid_points(self):
        points = [data.Point(1, 1), data.Point(3, 4), data.Point(0, 5)]
        result = lab5.furthest_from_origin(points)
        expected_index = 1
        self.assertEqual(result, expected_index)

    def test_furthest_from_origin_negative_coordinates(self):
        points = [data.Point(-1, -1), data.Point(-3, -4), data.Point(0, -5)]
        result = lab5.furthest_from_origin(points)
        expected_index = 1
        self.assertEqual(result, expected_index)

    def test_furthest_from_origin_empty_list(self):
        points = []
        result = lab5.furthest_from_origin(points)
        self.assertIsNone(result)

    def test_furthest_from_origin_single_point(self):
        points = [data.Point(2, 3)]
        result = lab5.furthest_from_origin(points)
        expected_index = 0
        self.assertEqual(result, expected_index)

if __name__ == '__main__':
    unittest.main()

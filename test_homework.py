from unittest import TestCase

import Homework2


class TestSumAllInList(TestCase):
    def test_sum_all_in_list(self):
        sum = Homework2.sum_all_in_list([4, 6, 2, 8, 5])
        self.assertEqual(sum, 25, "The addition here is not working")

        sum = Homework2.sum_all_in_list([-1, 0, -4])
        self.assertEqual(sum, -5, "Your sum method can't handle negative numbers")

    def test_merge_two_lists(self):
        merge = Homework2.merge_two_lists([[4, 2, 6], [2, 6, 8], [21, 2, 4]])
        self.assertEqual(merge, [4, 2, 6, 2, 6, 8, 21, 2, 4], "Your merge method isn't returning what I expected")

    def test_smallest_in_list(self):
        smallest = Homework2.get_smallest_number_in_list([2, 5, 7])
        self.assertEqual(smallest, 2, "Your smallest number method isn't returning what I expected")

        smallest = Homework2.get_smallest_number_in_list([5, 2, 7])
        self.assertEqual(smallest, 2, "Your smallest number method isn't returning what I expected")

        smallest = Homework2.get_smallest_number_in_list([2, 2, 6])
        self.assertEqual(smallest, 2, "Your smallest number method isn't returning what I expected")

        smallest = Homework2.get_smallest_number_in_list([2, -2, -7])
        self.assertEqual(smallest, -7, "Your smallest number method acts weirdly when the list has negatives in")

    def test_remove_even_numbers(self):
        removed = Homework2.return_odd_numbers([2, 3, 4])
        self.assertEqual(removed, [3], "Your remove even numbers method isn't returning what I expected")

        removed = Homework2.return_odd_numbers([4, 2, 6])
        self.assertEqual(removed, [], "Your remove even numbers method doesn't work when only even numbers are passed in")

        removed = Homework2.return_odd_numbers([1, 3, 5])
        self.assertEqual(removed, [1, 3, 5], "Your remove even numbers method doesn't work when only odd numbers are passed in")

    def test_append_to_all_elements(self):
        appended = Homework2.append_to_all_elements(["hey", "there", "friend"], "test")
        self.assertEqual(appended, ["heytest", "theretest", "friendtest"], "Your append to all elements isn't returning what I expected")

    def test_list_of_chars(self):
        chars = Homework2.list_of_characters_in_string("Hello")
        self.assertEqual(chars, ["H", "e", "l", "l", "o"], "Your list of characters in string method isn't working like I expected")





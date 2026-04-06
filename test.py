import unittest
from main import bubble_sort, binary_sort

class TestSortingAlgorithms(unittest.TestCase):

    def setUp(self):
        self.unsorted_list = [64, 34, 25, 12, 22, 11, 90]
        self.sorted_list = [11, 12, 22, 25, 34, 64, 90]

    def test_bubble_sort_basic(self):
        self.assertEqual(bubble_sort(self.unsorted_list.copy()), self.sorted_list)

    def test_binary_sort_basic(self):
        self.assertEqual(binary_sort(self.unsorted_list.copy()), self.sorted_list)

    def test_empty_list(self):
        self.assertEqual(bubble_sort([]), [])
        self.assertEqual(binary_sort([]), [])

    def test_duplicates(self):
        data = [3, 1, 3, 2, 1]
        expected = [1, 1, 2, 3, 3]
        self.assertEqual(bubble_sort(data.copy()), expected)
        self.assertEqual(binary_sort(data.copy()), expected)

    def test_already_sorted(self):
        self.assertEqual(bubble_sort(self.sorted_list.copy()), self.sorted_list)
        self.assertEqual(binary_sort(self.sorted_list.copy()), self.sorted_list)

    def test_negative_numbers(self):
        data = [-5, 2, -1, 0, 3]
        expected = [-5, -1, 0, 2, 3]
        self.assertEqual(bubble_sort(data.copy()), expected)
        self.assertEqual(binary_sort(data.copy()), expected)

if __name__ == '__main__':
    unittest.main()
import random
import sort
import unittest


# sort_func = sort.bubble_sort_v1
# sort_func = sort.bubble_sort_v2
# sort_func = sort.bubble_sort_v3
# sort_func = sort.bubble_sort
# sort_func = sort.selection_sort
# sort_func = sort.stable_selection_sort
# sort_func = sort.insertion_sort
# sort_func = sort.merge_sort
sort_func = sort.quick_sort
# sort_func = sort.counting_sort


class Test(unittest.TestCase):
    
    def test_empty_array(self):
        array = []
        result = sort_func(array)
        expected = sorted(array)
        self.assertEqual(result, expected)

    def test_single_element_array(self):
        array = [42]
        result = sort_func(array)
        expected = sorted(array)
        self.assertEqual(result, expected)

    def test_even_length_array(self):
        array = [random.randint(0, 10) for _ in range(4)]
        result = sort_func(array)
        expected = sorted(array)
        self.assertEqual(result, expected)
    
    def test_odd_length_array(self):
        array = [random.randint(0, 10) for _ in range(5)]
        result = sort_func(array)
        expected = sorted(array)
        self.assertEqual(result, expected)

    def test_small_array(self):
        array = [random.randint(-50, 50) for _ in range(20)]
        result = sort_func(array)
        expected = sorted(array)
        self.assertEqual(result, expected)
    
    def test_medium_array(self):
        array = [random.randint(-200, 200) for _ in range(100)]
        result = sort_func(array)
        expected = sorted(array)
        self.assertEqual(result, expected)
    
    def test_large_array(self):
        array = [random.randint(-1000, 1000) for _ in range(1000)]
        result = sort_func(array)
        expected = sorted(array)
        self.assertEqual(result, expected)
    
    def test_with_key(self):
        arr = ['Bellingham', 'Alice', 'Alfredo de', 'James', 'Jacob', 'John']
        result = sort_func(arr, key=len)
        expected = sorted(arr, key=len)
        self.assertEqual(result, expected)

    def test_stability(self):
        arr = [
            (23, "y"), (15, "m"), (10, "a"), (11, "c"), (5, "a"),
            (-5, "y"), (2, "b"), (0, "f"), (3, "y"), (10, "w")
        ]
        key=lambda x: ord(x[1])
        result = sort_func(arr, key=key)
        expected = sorted(arr, key=key)
        self.assertEqual(result, expected)

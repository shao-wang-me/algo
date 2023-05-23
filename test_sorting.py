from unittest import TestCase
from random import random
from sorting import sorting_algorithms

class TestSorting(TestCase):
  def setUp(self):
    self.cases = [
      [],
      [1],
      [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
      [4,2,1,6,8,3,1,3,7,9],
      [1,2,3,4,5,6,7,8,9,10,11,12,13],
      [-4,2,4,1,2,5,8,9,-12,28192,39,6.7],
      [5,4,3,2,1]
    ]

    for _ in range(1000):
      self.cases.append([random() - 0.5 for _ in range(1000)])  # random cases
      self.cases.append([1 for _ in range(100)])  # all equal cases

    print('generated test cases')

  def test_sorting(self):
    iteration_stats = {}
    for sort in sorting_algorithms:
      sorting_algorithm_name = sort.__name__
      iteration_stats[sorting_algorithm_name] = 0
      with self.subTest(sorting_algorith=sorting_algorithm_name):
        for nums in self.cases:
          # make copies of nums, in case the elements are accidentally modified
          sorted_nums, iterations = sort(nums[:])
          self.assertEqual(sorted_nums, sorted(nums[:]))
          iteration_stats[sorting_algorithm_name] += iterations
    print(iteration_stats)

if __name__ == '__main__':
  unittest.main()
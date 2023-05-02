from unittest import TestCase
from random import random
from sorting import sorting_algorithms

class TestSorting(TestCase):
  def setUp(self):
    self.cases = [
      [],
      [1],
      [4,2,1,6,8,3,1,3,7,9],
      [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
      [1,2,3,4,5,6,7,8,9,10,11,12,13],
      [-4,2,4,1,2,5,8,9,-12,28192,39,6.7],
      [5,4,3,2,1]
    ]

    for _ in range(100):
      self.cases.append([random() - 0.5 for _ in range(100)])

  def test_sorting(self):
    for sort in sorting_algorithms:
      with self.subTest(sorting_algorith=sort.__name__):
        for nums in self.cases:
          self.assertEqual(sort(nums), sorted(nums))

if __name__ == '__main__':
  unittest.main()
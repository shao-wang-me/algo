import math
import random

def random_pivot(nums, l, r):
  """Select a pivot randomly and put it to the front."""
  p = random.randint(l, r)
  pivot = nums[p]
  nums[l], nums[p] = pivot, nums[l]
  return pivot
  # return nums[l]

def partition_hoare(nums, l, r):
  pivot = random_pivot(nums, l, r)
  i, j = l + 1, r
  while i <= j:
    if nums[i] < pivot:
      i += 1
      continue
    if nums[j] >= pivot:
      j -= 1
      continue
    nums[i], nums[j] = nums[j], nums[i]
  nums[l], nums[j] = nums[j], pivot
  return j

def partition_hoare_repeat_until(nums, l, r):  # handle all equal cases better
  pivot = random_pivot(nums, l, r)             # because i++ and j-- when nums[i] == nums[j] == pivot
  i, j = l, r + 1
  while True:
    while True:
      i += 1
      if nums[i] >= pivot:
        break
    while True:
      j -= 1
      if nums[j] <= pivot:
        break
    nums[i], nums[j] = nums[j], nums[i]
    if i >= j:
      break
  nums[i], nums[j] = nums[j], nums[i]
  nums[l], nums[j] = nums[j], nums[l]
  return j

def partition_lomuto(nums, l, r):
  pivot = random_pivot(nums, l, r)
  j = l
  for i in range(l + 1, r + 1):
    if nums[i] < pivot:
      j += 1
      # must have nums[j] < pivot
      nums[i], nums[j] = nums[j], nums[i]
  # must have nums[j] < pivot
  nums[l], nums[j] = nums[j], pivot  # put pivot to the right place
  return j

def quicksort_core(nums, l, r, partition) -> int:  # returns the number of iterations
  if l < r:
    i = partition(nums, l, r)
    left_iterations = quicksort_core(nums, l, i - 1, partition)
    right_iterations = quicksort_core(nums, i + 1, r, partition)
    return max(left_iterations, right_iterations) + 1
  return 0

def quicksort_lomuto(nums):
  iterations = quicksort_core(nums, 0, len(nums) - 1, partition_lomuto)
  return nums, iterations

def quicksort_hoare(nums):
  iterations = quicksort_core(nums, 0, len(nums) - 1, partition_hoare)
  return nums, iterations

def quicksort_hoare_repeat_until(nums):
  nums.append(math.inf)  # append a sentinel to prevent index i from advancing beyond position n
  iterations = quicksort_core(nums, 0, len(nums) - 2, partition_hoare_repeat_until)  # thus r = n - 2 here
  return nums[:-1], iterations  # and remove the last math.inf

sorting_algorithms = [
  quicksort_lomuto,
  quicksort_hoare,
  quicksort_hoare_repeat_until
]
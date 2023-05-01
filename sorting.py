from random import randint

def lomuto_parition(nums, l, r):
  p = randint(l, r)  # Randomly pick a pivot
  pivot = nums[p]
  nums[l], nums[p] = pivot, nums[l]  # Put pivot at the front
  n = len(nums)
  j = l
  for i in range(l + 1, r + 1):
    if nums[i] < pivot:
      j += 1
      # Must have nums[j] < pivot
      nums[i], nums[j] = nums[j], nums[i]
  # Must have nums[j] < pivot
  nums[l], nums[j] = nums[j], pivot  # Put pivot to the right place
  return j

def quicksort_core(nums, l, r, partition):
  if l < r:
    i = partition(nums, l, r)
    quicksort_core(nums, l, i - 1, partition)
    quicksort_core(nums, i + 1, r, partition)

def quicksort_lomuto(nums):
  quicksort_core(nums, 0, len(nums) - 1, lomuto_parition)
  return nums

sorting_algorithms = [
  quicksort_lomuto
]
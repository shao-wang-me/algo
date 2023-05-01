from random import randint

def random_pivot(nums, l, r):
  """Select a pivot randomly and put it to the front."""
  p = randint(l, r)
  pivot = nums[p]
  nums[l], nums[p] = pivot, nums[l]
  return pivot

def partition_hoare(nums, l, r):
  pivot = random_pivot(nums, l, r)
  i, j = l + 1, r
  while i <= j:
    while nums[i] < pivot:
      i += 1
    while nums[j] >= pivot:
      i -= 1
    if i < j:
      nums[i], nums[j] = nums[j], nums[i]
  nums[l], nums[j] = nums[j], pivot

def partition_lomuto(nums, l, r):
  pivot = random_pivot(nums, l, r)
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
  quicksort_core(nums, 0, len(nums) - 1, partition_lomuto)
  return nums

def quicksort_hoare(nums):
  quicksort_core(nums, 0, len(nums) - 1, partition_lomuto)
  return nums

sorting_algorithms = [
  quicksort_lomuto,
  quicksort_hoare
]
# Two Integer Sum II
# Solved 
# Given an array of integers numbers that is sorted in non-decreasing order.

# Return the indices (1-indexed) of two numbers, [index1, index2], such that they add up to a given target number target and index1 < index2. Note that index1 and index2 cannot be equal, therefore you may not use the same element twice.

# There will always be exactly one valid solution.

# Your solution must use 
# O(1) additional space.

# Example 1:

# Input: numbers = [1,2,3,4], target = 3

# Output: [1,2]
# Explanation:
# The sum of 1 and 2 is 3. Since we are assuming a 1-indexed array, index1 = 1, index2 = 2. We return [1, 2].

# Constraints:

# 2 <= numbers.length <= 1000
# -1000 <= numbers[i] <= 1000
# -1000 <= target <= 1000

# class Solution:
#     def twoSum(self, numbers: List[int], target: int) -> List[int]:
#         for i in range(len(numbers)):
#             left = i + 1
#             right = len(numbers) - 1
#             tmp = target - numbers[i]
#             while left <= right:
#                 mid = left + (right - left)//2
#                 if numbers[mid] == tmp:
#                     return [i + 1, mid + 1]
#                 elif numbers[mid] < tmp:
#                     left = mid + 1
#                 else:
#                     right = mid - 1
#         return []

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        r = len(numbers) - 1
        l = 0
        while(l != r):
            tmp = numbers[l] + numbers[r]
            if(tmp == target):
                return[l+1,r+1]
            if(tmp < target):
                l +=1
            else:
                r-=1



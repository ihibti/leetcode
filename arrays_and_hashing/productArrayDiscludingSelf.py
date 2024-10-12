# Products of Array Discluding Self
# Solved 
# Given an integer array nums, return an array output where output[i] is the product of all the elements of nums except nums[i].

# Each product is guaranteed to fit in a 32-bit integer.

# Follow-up: Could you solve it in 
# O
# (
# n
# )
# O(n) time without using the division operation?

# Example 1:

# Input: nums = [1,2,4,6]

# Output: [48,24,12,8]
# Example 2:

# Input: nums = [-1,0,1,2,3]

# Output: [0,-6,0,0,0]
# Constraints:

# 2 <= nums.length <= 1000
# -20 <= nums[i] <= 20

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [0] * len(nums)
        pref = [nums[0]] * len(nums)
        suff = [nums[-1]] * len(nums)

        for i in range(1, len(nums)):
            pref[i] = pref[i - 1] * nums[i]
        
        for i in range(len(nums) - 2, -1, -1):
            suff[i] = suff[i + 1] * nums[i]
        
        res[0] = suff[1]
        res[-1] = pref[-2]
        for i in range(1, len(nums) - 1):
            res[i] = pref[i-1] * suff[i+1]

        return res


# alternative solution 
# def productExceptSelf(self, nums: List[int]) -> List[int]:
#         mul = 1
#         flag = 0
#         for n in nums:
#             if n != 0:
#                 mul *= n
#             elif n == 0 and flag == 0:
#                 flag = 1
#             else:
#                 mul = 0
#         ret = []
#         for n in nums:
#             if n != 0 and flag == 0:
#                 ret.append(mul // n)
#             elif n != 0 and flag == 1:
#                 ret.append(0)
#             else:
#                 ret.append(mul)
#         return ret
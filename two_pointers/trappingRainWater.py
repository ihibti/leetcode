# Trapping Rain Water
# Solved 
# You are given an array non-negative integers heights which represent an elevation map. Each value heights[i] represents the height of a bar, which has a width of 1.

# Return the maximum area of water that can be trapped between the bars.

# Example 1:



# Input: height = [0,2,0,3,1,0,1,3,2,1]

# Output: 9
# Constraints:

# 1 <= height.length <= 1000
# 0 <= height[i] <= 1000

def area(i, j, height, cache):
    for k in range(i+1, j):
        if height[k] >= height[i] or height[k] >= height[j]:
            return
    for k in range(i+1, j):
        if k not in cache:
            cache[k] = min(height[i], height[j]) - height[k]
        if k in cache:
            if min(height[i], height[j]) - height[k] > cache[k]:
                cache[k] = min(height[i], height[j]) - height[k]

class Solution:
    def trap(self, height: List[int]) -> int:
        cache = {}
        for i in range(len(height)):
            for j in range(i + 2, len(height)):
                area(i, j, height, cache)
        
        ret = 0
        for value in cache.values():
            ret += value
        return ret

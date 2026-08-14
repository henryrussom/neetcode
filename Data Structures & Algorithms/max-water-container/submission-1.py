class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left = 0
        right = len(heights) - 1
        value = 0
        while left < right:
            temp_value = min(heights[left],heights[right]) * (right - left)
            if temp_value > value: value = temp_value

            if heights[left] < heights[right]:
                left += 1
            else:
                right -= 1
            
        return value
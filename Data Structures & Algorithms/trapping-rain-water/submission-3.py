class Solution:
    def trap(self, height: List[int]) -> int:
        leftm = 0
        rightm = len(height) - 1
        left = 0
        right = len(height) - 1
        water = 0
        while left < right:
            if height[left] > height[leftm]: leftm = left
            if height[right] > height[rightm]: rightm = right

            if height[leftm] < height[rightm]:
                water += height[leftm] - height[left]
                left += 1
            else:
                water += height[rightm] - height[right]
                right -= 1
        return water    
        
            
class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        if len(nums) < 2: return nums

        left = 0
        right = 1
        temp = int

        while True:
            if nums[right] < nums[left]:
                temp = nums[left]
                nums[left] = nums[right]
                nums[right] = temp
                if left != 0:
                    left -= 1
                    right -= 1
            elif right != len(nums) - 1:
                left += 1
                right += 1
            else: return nums
        
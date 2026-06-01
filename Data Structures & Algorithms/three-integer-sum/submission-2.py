class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        for f in range(len(nums) - 1):
            s = f + 1
            t = len(nums) - 1
            while s < t:
                if nums[s] + nums[t] == -nums[f]:
                    if [nums[f], nums[s], nums[t]] not in res:
                        res.append([nums[f], nums[s], nums[t]])
                    s += 1
                    t -= 1
                elif nums[s] + nums[t] > -nums[f]:
                    t -= 1
                elif nums[s] + nums[t] < -nums[f]:
                    s += 1

                
        return res
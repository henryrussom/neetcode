class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        setn = set(nums)
        counter = 0
        maxn = 0
        for num in setn:
            if num - 1 not in setn:
                counter = 1
                while num + counter in setn:
                        counter += 1
                if counter > maxn: maxn = counter
        return maxn
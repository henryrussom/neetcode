class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        maxim = 0
        left = 0
        right = 0
        seen = set()
        while right < len(s):
            if s[right] in seen:
                seen.remove(s[left])
                left += 1
            else: 
                seen.add(s[right])
                right += 1

            if (right - left) > maxim: maxim = (right - left)
        return maxim
    
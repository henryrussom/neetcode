class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        maxim = 0
        chars = {}
        left = 0
        for right in range(len(s)):
            chars[s[right]] = chars.get(s[right], 0) + 1
            if (right - left + 1) - k <= max(chars.values()):
                maxim = max(maxim, right - left + 1)
            else:
                chars[s[left]] -= 1
                left += 1

        return maxim
class Solution:
    def isPalindrome(self, s: str) -> bool:
        i = 0
        l = len(s) - 1
        while i < l:
            while i < l and not s[i].isalnum():
                i += 1
            while i < l and not s[l].isalnum():
                l -= 1
            
            if s[i].lower() != s[l].lower():
                return False

            i += 1
            l -= 1
        
        return True

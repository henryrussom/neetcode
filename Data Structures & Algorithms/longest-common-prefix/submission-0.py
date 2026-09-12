class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        
        sofar = ""
        n = min(len(str) for str in strs)

        for i in range(n):
            cur = strs[0][i]
            for str in strs:
                if str[i] != cur:
                    return sofar

            sofar += cur

        return sofar
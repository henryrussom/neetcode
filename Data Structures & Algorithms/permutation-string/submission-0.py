class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        need = defaultdict(int)
        window = defaultdict(int)

        for i in range(len(s1)):
            need[s1[i]] += 1
            window[s2[i]] += 1

        if need == window:
            return True

        for i in range(len(s1), len(s2)):
            window[s2[i]] += 1
            left = s2[i - len(s1)]
            window[left] -= 1
            if window[left] == 0:
                del window[left]
            if need == window:
                return True

        return False
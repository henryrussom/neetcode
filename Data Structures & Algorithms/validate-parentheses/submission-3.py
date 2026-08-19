class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for p in s:
            if (p == "}"):
                if not stack or stack[-1] != "{":
                    return False
                stack.pop()
                continue

            if (p == "]"):
                if not stack or stack[-1] != "[":
                    return False
                stack.pop()
                continue

            if (p == ")"):
                if not stack or stack[-1] != "(":
                    return False
                stack.pop()
                continue

            stack.append(p)
        
        return not stack


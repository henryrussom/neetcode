class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for char in s:
            if (char == "(") or (char == "[") or (char == "{"):
                stack.append(char)
            elif not stack:
                return False

            if char == ")":
                popped = stack.pop()
                if popped != "(":
                    return False
            
            if char == "]":
                popped = stack.pop()
                if popped != "[":
                    return False
            
            if char == "}":
                popped = stack.pop()
                if popped != "{":
                    return False

        if stack: return False
        return True
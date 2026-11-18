class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for val in tokens:
            if val == "*" or val == "/" or val == "-" or val == "+":
                num1 = stack.pop()
                num2 = stack.pop()

                if val == "+":
                    stack.append(num2 + num1)
                elif val == "-":
                    stack.append(num2 - num1)
                elif val == "*":
                    stack.append(num2 * num1)
                else:
                    stack.append(int(num2 / num1))
            else:
                num = int(val)
                stack.append(num)
        return stack.pop()
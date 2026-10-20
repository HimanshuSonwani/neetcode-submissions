class Solution:
    def isValid(self, s: str) -> bool:
        stc = []

        for i in s:
            if i == '[' or i == '{' or i == '(':
                stc.append(i)

            else:
                if not stc:
                    return False

                if i == ']' and stc[-1] == '[':
                    stc.pop()
                elif i == '}' and stc[-1] == '{':
                    stc.pop()
                elif i == ')' and stc[-1] == '(':
                    stc.pop()
                else:
                    return False

        if not stc:
            return True
        else:
            return False
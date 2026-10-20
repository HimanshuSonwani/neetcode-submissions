class Solution:
    def isValid(self, s: str) -> bool:
        stc = []

        for a in s:
            if a == '[' or a == '{' or a == '(':
                stc.append(a)

            else:
                if not stc:
                    return False

                if a == ']' and stc[-1] == '[':
                    stc.pop()

                elif a == '}' and stc[-1] == '{':
                    stc.pop()

                elif a == ')' and stc[-1] == '(':
                    stc.pop()

                else:
                    return False

        return len(stc) == 0
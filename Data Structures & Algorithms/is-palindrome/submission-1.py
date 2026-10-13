class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = "".join(s.split())
        s = "".join(filter(str.isalnum, s)).lower()
        l = 0
        r = len(s) - 1
        while l < r:
            if s[l] == s[r]:
                l = l + 1
                r = r - 1
            else:
                break
        if l >= r:
            return True
        else:
            return False
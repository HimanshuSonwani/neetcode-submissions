class Solution:

    def encode(self, strs: List[str]) -> str:
        encodee = ''
        for i in range(len(strs)):
            encodee = encodee + str(len(strs[i])) + "#" + strs[i]
        return encodee

    def decode(self, s: str) -> List[str]:
        decodee = []
        i = 0
        while i < len(s):
            j = i
            while s[j] != "#":
                j = j + 1
            length = int(s[i:j])
            start = j + 1
            stop = j + 1 + length
            word = s[start:stop]
            decodee.append(word)
            i = stop
        return decodee
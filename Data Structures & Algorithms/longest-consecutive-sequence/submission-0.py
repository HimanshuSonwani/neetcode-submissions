class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        dic = {}
        for n in nums:
            if n in dic:
                dic[n] = dic[n] + 1
            else:
                dic[n] = 1
        s = set(dic.keys())
        out = []
        for i in s:
            if i-1 not in s:
                nn = i
                seq = [i]
                for j in range(len(s) - 1):
                    if nn + 1 in s:
                        nn = nn + 1
                        seq.append(nn)
                    else:
                        break
                if len(seq) > len(out):
                    out = seq
        return len(out)
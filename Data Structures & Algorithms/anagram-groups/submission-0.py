class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dic = {}
        for n in strs:
            keys = "".join(sorted(n))
            if keys in dic:
                dic[keys].append(n)
            else:
                dic[keys] = [n]
        return list(dic.values())
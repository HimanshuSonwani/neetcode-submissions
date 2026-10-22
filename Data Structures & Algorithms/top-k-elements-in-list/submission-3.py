class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dic = {}
        for n in nums:
            if n in dic:
                dic[n] = dic[n] + 1
            else:
                dic[n] = 1
        keys = sorted(dic, key=dic.get, reverse=True)
        return keys[:k]
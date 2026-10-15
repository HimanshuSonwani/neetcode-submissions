class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result = []

        for i in range(len(nums) - 2):
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            left = i + 1
            right = len(nums) - 1
            a = nums[i]

            while left < right:
                total = a + nums[left] + nums[right]

                if total == 0:
                    triple = [a, nums[left], nums[right]]

                    if triple not in result:
                        result.append(triple)

                    left = left + 1
                    right = right - 1

                elif total < 0:
                    left = left + 1

                else:
                    right = right - 1

        return result
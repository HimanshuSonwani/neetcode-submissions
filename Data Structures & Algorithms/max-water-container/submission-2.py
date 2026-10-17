class Solution:
    def maxArea(self, height: List[int]) -> int:
        left = 0
        right = len(height) - 1
        max_area = 0

        while left < right:
            h = min(height[left], height[right])
            width = right - left
            a = h * width

            max_area = max(max_area, a)

            if height[left] < height[right]:
                left = left + 1
            elif height[left] > height[right]:
                right = right - 1
            else:
                right = right - 1

        return max_area
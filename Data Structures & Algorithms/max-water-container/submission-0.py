class Solution:
    def maxArea(self, heights: List[int]) -> int:
        max_area = min(heights[0], heights[-1]) * (len(heights) - 1)
        if len(heights) == 2:
            return max_area
        l, r = 0, len(heights) -1
        while l < r:
            new_area = min(heights[l], heights[r]) * (r - l)
            max_area = new_area if new_area > max_area else max_area
            if heights[l] < heights[r]:
                l += 1
            else:
                r -= 1
        return max_area
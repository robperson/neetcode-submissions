class Solution:
    def trap(self, height: List[int]) -> int:
        left_maxes = [0] * len(height)
        right_maxes = [0] * len(height)
        left_max = 0
        right_max = 0

        '''
        [0,2,0,3,1,0,1,3,2,1]
        9
        [0,0,2,2,3,3,3,3,3,3]
        [3,3,3,3,3,3,3,2,1,0]
        '''
        for i, val in enumerate(height):
            left_maxes[i] = left_max
            if val > left_max:
                left_max = val
        for i in range(len(right_maxes) - 1, -1, -1):
            val = height[i]
            right_maxes[i] = right_max
            if val > right_max:
                right_max = val
        max_area = 0

        for i, h in enumerate(height):
            a = min(left_maxes[i], right_maxes[i]) - h
            if a > 0:
                max_area += a
        return max_area
        
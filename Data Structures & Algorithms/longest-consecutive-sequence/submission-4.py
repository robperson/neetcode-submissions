class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        '''
        [2,20,4,10,3,4,5]

        [2,3,4,4,5,10,20]
         s
             e
        '''
        if not nums:
            return 0
        nums.sort()
        unique_nums = sorted(list(set(nums)))
        win_start, win_end = 0, 0
        max_window = 1
        while win_start < len(unique_nums) and win_end < len(unique_nums) - 1:
            curr_num = unique_nums[win_end]
            next_num = unique_nums[win_end + 1]
            if next_num == curr_num + 1:
                win_end += 1
                max_window = max(max_window, win_end - win_start + 1)
            else:
                win_start = win_end + 1
                win_end = win_end + 1
            
        return max_window
        

        
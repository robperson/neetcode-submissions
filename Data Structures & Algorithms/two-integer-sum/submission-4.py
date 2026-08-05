class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        left, right = 0, len(nums) - 1
        sorted_nums = sorted((num, idx) for idx, num in enumerate(nums))
        print(f"{sorted_nums=}")
        while left < right:
            current_sum = sorted_nums[left][0] + sorted_nums[right][0]
            left_idx, right_idx = sorted_nums[left][1], sorted_nums[right][1]
            if current_sum == target:
                return [min(left_idx, right_idx), max(left_idx, right_idx)]
            elif current_sum > target:
                right -= 1
            else: # must be less than target
                left += 1
        return []
        
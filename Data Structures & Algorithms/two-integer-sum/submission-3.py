class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # left, right = 0, len(nums) - 1
        # sorted_nums = sorted((num, idx) for idx, num in enumerate(nums))
        # print(f"{sorted_nums=}")
        # while right > left:
        #     current_sum = nums[left] + nums[right]
        #     left_idx, right_idx = sorted_nums[left][1], sorted_nums[right][1]
        #     if current_sum == target:
        #         return [min(left_idx, right_idx), max(left_idx, right_idx)]
        #     elif current_sum > target:
        #         right -= 1
        #     else: # must be less than target
        #         left += 1
        A = []
        for i, num in enumerate(nums):
            A.append([num, i])

        A.sort()
        i, j = 0, len(nums) - 1
        while i < j:
            cur = A[i][0] + A[j][0]
            if cur == target:
                return [min(A[i][1], A[j][1]),
                        max(A[i][1], A[j][1])]
            elif cur < target:
                i += 1
            else:
                j -= 1
        return []
        
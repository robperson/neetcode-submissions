class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        current_pos = 0
        end = len(nums) - 1
        result = []
        for i, num in enumerate(nums):
            if num > 0:
                break
            
            # skip duplicates
            if i > 0 and num == nums[i-1]:
                continue
            j, k = i + 1, end
            while j < k:
                three_sum = num + nums[j] + nums[k]
                if three_sum == 0:
                    result.append([num, nums[j], nums[k]])
                    j += 1
                    k -= 1
                    while j < k and nums[j] == nums[j - 1]:
                        j += 1
                elif three_sum < 0:
                    j += 1
                else:
                    k -= 1
        return result

        
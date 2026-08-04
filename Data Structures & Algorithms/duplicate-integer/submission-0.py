from collections import Counter

class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        if not nums:
            return False
        counts = Counter(nums)
        return any(v for v in counts.values() if v > 1)
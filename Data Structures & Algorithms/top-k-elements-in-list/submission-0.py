from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = Counter(nums)
        nums_by_count_order = [(count, num) for num, count in counts.items()]
        nums_by_count_order.sort(reverse=True)
        return [num for _, num in nums_by_count_order[:k]]
        
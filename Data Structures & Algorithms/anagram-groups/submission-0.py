from collections import Counter, defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = defaultdict(list)
        for str in strs:
            key = "".join(sorted(str))
            groups[key].append(str)
        result = []
        for anagrams in groups.values():
            result.append(anagrams)
        return result
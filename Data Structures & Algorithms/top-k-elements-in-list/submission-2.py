from collections import Counter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = Counter(nums)
        return sorted(freq.keys(), key=lambda x: freq[x])[::-1][:k]
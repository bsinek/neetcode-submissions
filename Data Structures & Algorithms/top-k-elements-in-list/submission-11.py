class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = Counter(nums)
        return list(sorted(freq.keys(), key = lambda x: freq[x], reverse=True))[:k]
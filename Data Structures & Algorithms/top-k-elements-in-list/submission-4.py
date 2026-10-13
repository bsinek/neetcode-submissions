from collections import Counter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = Counter(nums)
        buckets = [[] for _ in range(len(nums) + 1)]
        for num, count in freq.items():
            buckets[count].append(num)
        res = []
        i = len(buckets) - 1
        while len(res) < k and i > 0:
            res += buckets[i]
            i -= 1
        return res
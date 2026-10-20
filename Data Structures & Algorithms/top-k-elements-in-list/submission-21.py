from collections import Counter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = Counter(nums)
        freq = [[] for _ in range(len(nums) + 1)]
        for num, count in counts.items():
            freq[count].append(num)

        res = []
        for i in range(len(nums), 0, -1):
            res += freq[i]
            if len(res) >= k:
                return res[:k]
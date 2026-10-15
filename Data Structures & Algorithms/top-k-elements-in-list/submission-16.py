from collections import Counter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = Counter(nums)
        groups = [[] for _ in range(len(nums) + 1)]
        for num, freq in counts.items():
            groups[freq].append(num)
        res = []
        for i in range(len(nums), 0, -1):
            res += groups[i]
            if len(res) == k:
                break
        return res[:k]
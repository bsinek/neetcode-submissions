from collections import Counter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = Counter(nums)
        groups = [[] for _ in range(len(nums) + 1)]
        for num, freq in counts.items():
            groups[freq].append(num)
        res = []
        i = len(nums)
        while len(res) < k:
            res += groups[i]
            i -= 1
        return res[:k]

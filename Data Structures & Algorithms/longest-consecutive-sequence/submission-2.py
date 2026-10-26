class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0: return 0

        hashset = set(nums)
        curr = min(hashset)
        best = 1
        streak = 1
        while len(hashset) > 1:
            if curr + 1 in hashset:
                hashset.remove(curr)
                curr += 1
                streak += 1
                best = max(best, streak)
            else:
                hashset.remove(curr)
                curr = min(hashset)
                streak = 1
        return best
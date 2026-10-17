class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def feasible(k):
            hours_used = 0
            for pile in piles:
                hours_used += (pile + k - 1) // k
            return hours_used <= h

        lo, hi = 1, max(piles)
        while lo < hi:
            mid = (lo + hi) // 2
            if feasible(mid):
                hi = mid
            else:
                lo = mid + 1
        return lo

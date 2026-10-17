class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def feasible(k):
            hours_used = 0
            for pile in piles:
                hours_used += (pile + k - 1) // k
            return hours_used <= h

        lo = 1
        hi = best = sum(piles)
        while lo <= hi:
            mid = (lo + hi) // 2
            if feasible(mid):
                best = min(best, mid)
                hi = mid - 1
            else:
                lo = mid + 1
        return best

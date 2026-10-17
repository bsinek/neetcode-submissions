class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        res = [pivot] * len(nums)
        l, r = 0, len(nums) - 1
        for num in nums:
            if num < pivot:
                res[l] = num
                l += 1
        for num in reversed(nums):
            if num > pivot:
                res[r] = num
                r -= 1
        return res

class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        res = [pivot] * len(nums)
        i = 0
        for num in nums:
            if num < pivot:
                res[i] = num
                i += 1

        j = len(nums) - 1
        for num in reversed(nums):
            if num > pivot:
                res[j] = num
                j -= 1
        return res
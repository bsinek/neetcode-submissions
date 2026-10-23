class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        ltr = [1] * len(nums)
        prod = 1
        for i in range(len(nums)):
            prod *= nums[i]
            ltr[i] = prod
        rtl = [1] * len(nums)
        prod = 1
        for i in range(len(nums) - 1, -1, -1):
            prod *= nums[i]
            rtl[i] = prod
    
        res = [1] * len(nums)
        for i in range(len(nums)):
            if i == 0:
                res[i] = rtl[i + 1]
            elif i == len(nums) - 1:
                res[i] = ltr[i - 1]
            else:
                res[i] = ltr[i - 1] * rtl[i + 1]
        return res

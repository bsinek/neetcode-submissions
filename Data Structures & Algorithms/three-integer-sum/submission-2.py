class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        for i, num in enumerate(nums):
            if num * 3 > 0:
                break
            if i != 0 and num == nums[i - 1]:
                continue

            lo, hi = i + 1, len(nums) - 1
            while lo < hi:
                total = num + nums[lo] + nums[hi]
                if total == 0:
                    res.append([num, nums[lo], nums[hi]])
                    lo += 1
                    hi -= 1
                    while lo < hi and nums[lo] == nums[lo - 1]:
                        lo += 1
                elif total < 0:
                    lo += 1
                else:
                    hi -= 1
        return res
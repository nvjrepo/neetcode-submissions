class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        a = {}
        for i in range(len(nums)):
            diff = target - nums[i]

            if a.get(nums[i], -1) != -1:
                return [a.get(nums[i]), i]
            a[diff] = i
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        
        for i in range(len(nums)):
            # break coz i > 0, the rest are > 0, sum can't = 0
            if nums[i] > 0:
                break
            
            # skip all item < num[i] once we found a match
            j = i + 1
            k = len(nums) - 1
            target = -nums[i]

            if i != 0 and nums[i] == nums[i-1]:
                continue

            while j < k:
                total = nums[j] + nums[k]
                if total < target:
                    j += 1
                elif total > target:
                    k -= 1
                elif j != i+1 and nums[j] == nums[j-1]:
                    j += 1
                else:
                    res.append([-target, nums[j], nums[k]])
                    j += 1

        return res

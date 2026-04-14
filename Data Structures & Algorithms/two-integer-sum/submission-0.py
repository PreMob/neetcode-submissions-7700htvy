class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        h = {}
        
        for i in range(len(nums)):
            sum = target - nums[i]

            if sum in h :
                return [h[sum],i]

            h[nums[i]] = i

        return []
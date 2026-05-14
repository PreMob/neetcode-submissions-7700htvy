class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        map = dict()
        res = set()
        n = len(nums) // 3

        for i in nums:
            if i in res:
                continue
            
            if i in map:
                map[i] += 1
            else:
                map[i] = 1

            if map[i] > n:
                res.add(i)

        return list(res)
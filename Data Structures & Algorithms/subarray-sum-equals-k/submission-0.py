class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        count=0
        ht={0:1}
        prefix_sum=0

        for num in nums:
            prefix_sum += num

            if (prefix_sum - k) in ht:
                count+=ht[prefix_sum - k]

            ht[prefix_sum] = ht.get(prefix_sum, 0)+1

        return count 
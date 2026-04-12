class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        n = len(nums)
        m = 2*n
        result = list()

        for num in range(m):
            result.append(nums[num%n])

        return result

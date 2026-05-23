class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        st = set(nums)
        longest = 0

        for num in st:
            if num-1 not in st:
                ln = 1
                while num+ln in st:
                    ln += 1
                longest = max(longest,ln)

        return longest
class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        if len(nums) == 1:
            return nums

        mid = int(len(nums)/2)

        left = self.sortArray(nums[:mid])
        right = self.sortArray(nums[mid:])

        return self.merge(left,right)

    def merge(self, l1: List[int], l2: List[int]) -> List[int]:
        combined = []

        i = 0
        j = 0

        while i < len(l1) and j < len(l2):
            if l1[i] < l2[j]:
                combined.append(l1[i])
                i += 1
            else:
                combined.append(l2[j])
                j += 1

        while i < len(l1):
            combined.append(l1[i])
            i += 1

        while j < len(l2):
            combined.append(l2[j])
            j += 1

        return combined
class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """

        n = len(s) - 1
        i = 0

        while i < n  :
            s[i],s[n] = s[n],s[i]
            i += 1
            n -= 1

        
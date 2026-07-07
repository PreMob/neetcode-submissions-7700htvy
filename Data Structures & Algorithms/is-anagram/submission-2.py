class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        d = {}
        d2 = {}

        for i in s:
            if i in d:
                d[i] += 1
            else:
                d[i] = 1

        for i in t:
            if i in d2:
                d2[i] += 1
            else:
                d2[i] = 1

        if (d == d2) == True:
            return True

        return False


class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        m, n = len(s1), len(s2)

        if m > n:
            return False

        s1_count = [0] * 26
        window = [0] * 26

        for ch in s1:
            s1_count[ord(ch) - ord('a')] += 1

        for i in range(m):
            window[ord(s2[i]) - ord('a')] += 1

        if s1_count == window:
            return True

        left = 0

        for right in range(m, n):
            # add new character
            window[ord(s2[right]) - ord('a')] += 1

            # remove old character
            window[ord(s2[left]) - ord('a')] -= 1
            left += 1

            if window == s1_count:
                return True

        return False
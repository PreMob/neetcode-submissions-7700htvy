class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""

        prefix = strs[0]

        for st in strs:
            i = 0
            while i < len(prefix) :
                if i== len(st) or prefix[i] != st[i]:
                    prefix = prefix[:i]
                    if prefix == "":
                        return prefix
                    break
                i += 1

        return prefix
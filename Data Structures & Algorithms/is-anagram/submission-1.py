class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        smap = {}
        tmap = {}
        n = len(s)
        m = len(t)

        if n != m :
            return False

        for i in range(n):
            if s[i] in smap:
                smap[s[i]] += 1
            else:
                smap[s[i]] = 1
            
            if t[i] in tmap:
                tmap[t[i]] += 1
            else:
                tmap[t[i]] = 1

        if smap == tmap :
            return True
        
        return False
        
        
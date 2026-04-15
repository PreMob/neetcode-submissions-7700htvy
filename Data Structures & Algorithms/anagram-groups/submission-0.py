class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        if not strs:
            return []
        elif len(strs) == 1:
            return [[strs[0]]]

        result = []
        hmap = []
        for st in strs:
            h = {}
            a = False
            
            for i in st:
                if i in h:
                    h[i]+=1
                else:
                    h[i]=0

            for j in range(len(hmap)):
                if hmap[j] == h:
                    result[j].append(st)  
                    a = True
            
            if a == False:
                hmap.append(h)
                result.append([st])

        return result


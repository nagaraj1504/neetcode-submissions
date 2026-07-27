class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        a=defaultdict(list)
        for c in strs:
            count=[0]*26
            for b in c:
                count[ord(b)-ord('a')]+=1
            a[tuple(count)].append(c)
        return list(a.values())
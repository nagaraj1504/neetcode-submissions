class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        a=defaultdict(list)
        for b in strs:
            count=[0]*26
            for c in b:
                count[ord(c)-ord('a')]+=1
            a[tuple(count)].append(b)
        return list(a.values())

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s1 = defaultdict(int)
        t1 = defaultdict(int)
        for l in s:
            s1[l] += 1
        for l in t:
            t1[l] += 1
        return s1 == t1

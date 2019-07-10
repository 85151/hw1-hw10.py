class Solution(object):
    def findTheDifference(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        d1 = collections.defaultdict(int)
        d2 = collections.defaultdict(int)
        for i in s:
            d1[i] += 1
        for i in t:
            d2[i] += 1
        for i in d2:
            if d1[i] != d2[i]:
                return i

class Solution:
    def heightChecker(self, heights):
        a = sorted(heights)
        return sum([1 for i in range(len(heights)) if (a[i] != heights[i])])

class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        import math
        if n<=0:
            return False
        elif round(math.log(n,2),9)==float(int(math.log(n,2))):
            return True
        else:
            return False

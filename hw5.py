class Solution:
    def numJewelsInStones(self, J: str, S: str) -> int:
        a=0
        if(len(J)<len(S)):
            b=J
            J=S
            S=b        
        for i in range(0,len(J),1):
            for f in range(0,len(S),1):
                if(J[i]==S[f]):
                    a+=1
        return a

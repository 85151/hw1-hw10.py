class Solution:
    def fib(self, N: int) -> int:
     
		
        store = [0,1]
        i = 2
        while i <= N:
            store.append(store[i-1]+store[i-2])
            i += 1
        return store[N]

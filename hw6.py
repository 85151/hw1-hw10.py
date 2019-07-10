class Solution:
	def checkPossibility(self, nums: List[int]) -> bool:
		stack=[]
		a=nums[:]
		b=nums[:]
		for i in range(len(nums)):
			if i>=1 and nums[i]<nums[i-1]:      
				a[i]=a[i-1]          
				b[i-1]=b[i]
				break
		if a==sorted(a) or b==sorted(b):
			return True
		else:
			return False

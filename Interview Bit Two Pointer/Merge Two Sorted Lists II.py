class Solution:
	# @param A : list of integers
	# @param B : list of integers
	def merge(self, A, B):

		A.extend(B)
		A.sort()

		return A


ans = Solution()
A = [1,5,8]
B = [6,9]
print(ans.merge(A,B))
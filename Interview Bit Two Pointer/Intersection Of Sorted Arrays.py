class Solution:
	# @param A : tuple of integers
	# @param B : tuple of integers
	# @return a list of integers
	def intersect(self, A, B):

		output = []
		n,m = len(A), len(B)
		i, j = 0,0
		while i < n and j < m:
			if A[i] > B[j]:
				j += 1
			elif A[i] < B[j]:
				i += 1
			else:
				output.append(A[i])
				i += 1
				j += 1
		return output

ans = Solution()

A = [1 ,2, 3, 3 ,4 ,5 ,6]
B = [3,3 ,5]
print(ans.intersect(A,B))

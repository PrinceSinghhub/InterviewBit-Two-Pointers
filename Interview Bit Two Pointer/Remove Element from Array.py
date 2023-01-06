# optmize code
class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def removeElement(self, A, B):
        n, curr = len(A), 0
        for i in range(n):
            if A[i] != B:
                A[curr] = A[i]
                curr += 1
        A = A[:curr]
        return curr
# class Solution:
#     # @param A : list of integers
#     # @param B : integer
#     # @return an integer
#     def removeElement(self, A, B):

#         while B in A:
#             A.remove(B)

#         return len(A)

ans = Solution()
arr = [4, 1, 1, 2, 1, 3]
B = 1
print(ans.removeElement(arr,B))

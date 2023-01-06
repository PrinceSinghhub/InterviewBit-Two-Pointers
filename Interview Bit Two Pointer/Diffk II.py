class Solution:
    # @param A : tuple of integers
    # @param B : integer
    # @return an integer
    def diffPossible(self, A, B):
        int_dict = {}
        for a in A:
            if a+B in int_dict or a-B in int_dict:
                # print(a, B-a, a-B)
                return 1
            else:
                int_dict[a] = 1
        return 0


ans = Solution()
A = [1,5,3]
k = 2
print(ans.diffPossible(A,k))
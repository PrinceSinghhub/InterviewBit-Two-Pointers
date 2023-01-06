class Solution:
    # @param A : list of integers
    # @return an integer
    def removeDuplicates(self, A):

        arr = []
        for i in A:
            if i not in arr:
                arr.append(i)
            else:
                continue
        arr.sort()
        A[:] = arr
        return len(A)


ans = Solution()
A = [1, 2, 2, 3, 3]
print(ans.removeDuplicates(A))
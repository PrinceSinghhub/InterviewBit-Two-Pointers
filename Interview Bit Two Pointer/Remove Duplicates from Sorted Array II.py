class Solution:
    # @param A : list of integers
    # @return an integer
    def removeDuplicates(self, A):

        ans = []
        for i in A:
            if i not in ans and ans.count(i) < 2:
                ans.append(i)
            elif i in ans and ans.count(i) < 2:
                ans.append(i)
        ans.sort()
        A[:] = ans
        print(A)
        return len(A)

ans = Solution()
A = [1,1,1,2]
print(ans.removeDuplicates(A))
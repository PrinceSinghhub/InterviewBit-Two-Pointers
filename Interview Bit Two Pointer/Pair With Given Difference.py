class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def solve(self, A, B):
        l=len(A)
        A=set(A)
        if(B==0):
            if(l!=len(A)):
                return 1
            return 0
        else:
            for i in A:
                if((B+i)in A):
                    return 1
            return 0



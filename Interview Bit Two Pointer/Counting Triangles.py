def binary_search(a, i):
    MOD = 1000000007
    lo = 0
    hi = i-1
    ans = 0
    while lo < hi:
        if a[lo]+a[hi] > a[i]:
            ans = (ans+hi-lo)%MOD
            hi = hi-1
        else:
            lo = lo+1
    return ans

class Solution:
    # @param A : list of integers
    # @return an integer
    def nTriang(self, A):
        MOD = 1000000007
        n = len(A)
        A.sort()
        ans = 0
        for i in range(n-1, 1, -1):
                ans =(ans+binary_search(A, i))%MOD
        return ans

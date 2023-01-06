class Solution:
    # @param A : integer
    # @param B : integer
    # @param C : integer
    # @return an integer
    def solve(self, A, B, C):
        ans=[]
        def pal(n):
            x=0
            while(n):
                x=x*10+n%10;
                n/=10;
            return x
        for i in range(A,B+1):
            #if pal(i)==i:
            if str(i)==str(i)[::-1]:
                ans.append(i)
        if len(ans)==0:
            return 0
        res=1
        for i in range(len(ans)-1,0,-1):
            j=0
            while j<i:
                if abs(ans[i]-ans[j])<=C:
                    res = max(res, i-j+1)
                    break
                j+=1
        return res


ans = Solution()
A = 80
B = 110
C = 10
print(ans.solve(A,B,C))
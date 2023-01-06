class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def solve(self, A, B):
        h = [0 for _ in range(len(A) + 1)]
        cnt = 0
        start = 0
        end = 0
        ans = 0
        p = 0
        while (end < len(A)):
            if h[A[end]] == 0:
                cnt += 1

            h[A[end]] += 1
            end += 1

            if cnt > B:
                p = 0
                h[A[start]] -= 1
                start += 1
                cnt -= 1

            while h[A[start]] > 1:
                h[A[start]] -= 1
                start += 1
                p += 1

            if cnt == B:
                ans += p + 1

        return ans

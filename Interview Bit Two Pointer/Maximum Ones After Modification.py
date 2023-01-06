def longestSubSeg(a, n, k):
    cnt0 = 0
    l = 0
    max_len = 0;

    # i decides current ending point
    for i in range(0, n):
        if a[i] == 0:
            cnt0 += 1

        # If there are more 0's move
        # left point for current
        # ending point.
        while (cnt0 > k):
            if a[l] == 0:
                cnt0 -= 1
            l += 1

        max_len = max(max_len, i - l + 1);

    return max_len


class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def solve(self, A, B):
        return longestSubSeg(A, len(A), B)
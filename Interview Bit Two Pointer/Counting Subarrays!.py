# Function to find number of subarrays
# having sum less than k.
def countSubarray(arr, n, k):
    count = 0

    for i in range(0, n):
        sum = 0;
        for j in range(i, n):

            # If sum is less than k
            # then update sum and
            # increment count
            if (sum + arr[j] < k):
                sum = arr[j] + sum
                count += 1
            else:
                break
    return count;


class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def solve(self, A, B):
        return countSubarray(A, len(A), B)

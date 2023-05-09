def main():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    ans = 0
    sum = 0
    right = 0
    for left in range(N):
        while right < N and sum < K:
            sum += A[right]
            right += 1
        if sum >= K:
            ans += N - right + 1
        sum -= A[left]
    print(ans)
main()
This is a typical problem that can be solved with the two-pointer algorithm. Let’s see how it works.
First, we fix the left end of the range, and move the right end to the right as far as possible. If the sum of the elements in the range exceeds K, we add the number of elements in the range to the answer. Then, we move the left end of the range to the right.
If we implement this algorithm in a straightforward way, the time complexity will be O(N^2). However, we can improve the time complexity to O(N) by using a data structure that allows us to quickly calculate the sum of the elements in the range. In this case, we can use a prefix sum.
Let’s see how we can use the prefix sum to improve the time complexity. Let’s say that we have a sequence A of length N, and we want to calculate the sum of the elements in the range A[l..r]. We can use the following formula to calculate the sum of the elements in the range A[l..r] in O(1) time.
A[l] + A[l+1] + … + A[r] = A[r+1] + A[r+2] + … + A[N] – (A[1] + A[2] + … + A[l-1])
The prefix sum A[r+1] + A[r+2] + … + A[N] is the sum of the elements in the range A[r+1..N], and the prefix sum A[1] + A[2] + … + A[l-1] is the sum of the elements in the range A[1..l-1]. Therefore, we can calculate the sum of the elements in the range A[l..r] in O(1) time.
Now, let’s see how we can use the prefix sum to solve the problem. Let’s say that we have a sequence A

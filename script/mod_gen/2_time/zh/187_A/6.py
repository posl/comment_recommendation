def solve(N, A):
    ans = 0
    A.sort()
    for i in range(N):
        ans += (2 * i - N + 1) * A[i]
    return ans
N = int(input())
A = list(map(int, input().split()))
print(solve(N, A))

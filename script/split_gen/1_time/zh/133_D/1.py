def solve(N, A):
    ans = [0] * N
    for i in range(N):
        ans[i] = A[i] * 2
    for i in range(N):
        ans[i] -= sum(ans) / 2
    return ans
N = int(input())
A = list(map(int, input().split()))
print(*solve(N, A))

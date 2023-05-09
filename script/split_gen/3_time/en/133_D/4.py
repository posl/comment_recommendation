def solve():
    N = int(input())
    A = list(map(int, input().split()))
    ans = [0] * N
    for i in range(N):
        ans[i] = A[i] - A[i-1]
    for i in range(N):
        if i % 2 == 0:
            ans[i] = -ans[i]
    for i in range(N):
        ans[i] += ans[i-1]
    for i in range(N):
        ans[i] //= 2
    print(*ans)

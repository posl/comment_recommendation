def solve():
    N = int(input())
    S = list(map(int, input().split()))
    T = list(map(int, input().split()))
    ans = [0] * N
    for i in range(N):
        ans[i] = T[i]
    for i in range(1, N):
        ans[i] = min(ans[i], ans[i - 1] + S[i - 1])
    for i in range(N):
        ans[i] = min(ans[i], ans[(i - 1 + N) % N] + S[(i - 1 + N) % N])
    for i in range(N):
        print(ans[i])

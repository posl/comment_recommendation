def solve():
    N = int(input())
    S = list(map(int, input().split()))
    T = list(map(int, input().split()))
    ans = [0] * N
    for i in range(N):
        if i == 0:
            ans[i] = T[i]
        else:
            ans[i] = min(T[i], ans[i - 1] + S[i - 1])
    for i in range(N):
        print(ans[i])
solve()

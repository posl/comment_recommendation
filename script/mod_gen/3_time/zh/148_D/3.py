def solve():
    N = int(input())
    A = list(map(int, input().split()))
    if N == 1:
        print(0)
        return
    if A[0] != 1:
        print(-1)
        return
    L = [0] * (N + 1)
    for i in range(N):
        L[i + 1] = L[i] + 1 if A[i] != A[i - 1] else L[i]
    ans = 0
    for i in range(1, N + 1):
        if L[i] < i:
            ans += 1
    print(ans)
solve()

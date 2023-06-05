def solve():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    S = [0] * (N + 1)
    for i in range(N):
        S[i + 1] = S[i] + A[i]
    dic = {}
    for s in S:
        r = s % M
        if r in dic:
            dic[r] += 1
        else:
            dic[r] = 1
    ans = 0
    for v in dic.values():
        ans += v * (v - 1) // 2
    print(ans)
solve()

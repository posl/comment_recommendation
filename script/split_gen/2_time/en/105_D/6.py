def solve():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    A = [a % M for a in A]
    A = [0] + A
    for i in range(N):
        A[i + 1] += A[i]
        A[i + 1] %= M
    from collections import defaultdict
    d = defaultdict(int)
    for a in A:
        d[a] += 1
    ans = 0
    for k, v in d.items():
        ans += (v * (v - 1)) // 2
    print(ans)

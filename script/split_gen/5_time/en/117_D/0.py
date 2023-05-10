def solve():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    ans = 0
    for i in range(40, -1, -1):
        cnt = 0
        for a in A:
            if a >> i & 1:
                cnt += 1
        if cnt < N - cnt and ans + (1 << i) <= K:
            ans += 1 << i
    f = 0
    for a in A:
        f += ans ^ a
    print(f)

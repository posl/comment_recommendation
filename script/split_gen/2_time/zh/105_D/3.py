def solve():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    # 从左到右累积和
    S = [0] * (N + 1)
    for i in range(N):
        S[i + 1] = S[i] + A[i]
    # 从左到右的累积和对M取余数
    for i in range(N + 1):
        S[i] %= M
    # 求每个余数的个数
    from collections import defaultdict
    dic = defaultdict(int)
    for i in range(N + 1):
        dic[S[i]] += 1
    # 求组合数
    ans = 0
    for v in dic.values():
        ans += v * (v - 1) // 2
    print(ans)
solve()

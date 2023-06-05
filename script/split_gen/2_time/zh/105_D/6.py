def solve():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    # 从左到右累积和
    S = [0] * (N + 1)
    for i in range(N):
        S[i + 1] = S[i] + A[i]
    # 余数的出现次数
    cnt = [0] * M
    for i in range(N + 1):
        cnt[S[i] % M] += 1
    # 组合
    ans = 0
    for c in cnt:
        ans += c * (c - 1) // 2
    print(ans)

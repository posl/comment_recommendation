def solve():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    # Aの累積和のmod M
    # 累積和のmod Mが同じになる区間の個数を求める
    s = [0] * (N + 1)
    for i in range(N):
        s[i + 1] = (s[i] + A[i]) % M
    from collections import defaultdict
    dd = defaultdict(int)
    for v in s:
        dd[v] += 1
    ans = 0
    for v in dd.values():
        ans += v * (v - 1) // 2
    print(ans)

if __name__ == '__main__':
    solve()
def solve():
    S = input()
    N = len(S)
    S = [int(c) for c in S]
    S.reverse()
    ans = 0
    cnt = [0] * 2019
    cnt[0] = 1
    d = 1
    cur = 0
    for i in range(N):
        cur = (cur + S[i] * d) % 2019
        d = d * 10 % 2019
        ans += cnt[cur]
        cnt[cur] += 1
    print(ans)
solve()

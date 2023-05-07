def solve():
    N, K = map(int, input().split())
    S = [input() for _ in range(N)]
    ans = 0
    for i in range(1 << N):
        cnt = 0
        for j in range(N):
            if i >> j & 1:
                cnt += 1
        if cnt != K:
            continue
        tmp = 0
        for j in range(26):
            ok = True
            for k in range(N):
                if i >> k & 1:
                    if chr(ord('a') + j) not in S[k]:
                        ok = False
            if ok:
                tmp += 1
        ans = max(ans, tmp)
    print(ans)

if __name__ == '__main__':
    solve()
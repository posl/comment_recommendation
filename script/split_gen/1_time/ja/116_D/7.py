def main():
    from sys import stdin
    input = stdin.readline
    N, K = map(int, input().split())
    td = [list(map(int, input().split())) for _ in range(N)]
    td.sort(key=lambda x:x[1], reverse=True)
    ans = 0
    cnt = [0]*(N+1)
    kind = 0
    for i in range(K):
        t, d = td[i]
        ans += d
        cnt[t] += 1
        if cnt[t] == 1:
            kind += 1
    ans += kind**2
    for i in range(K, N):
        t, d = td[i]
        if cnt[t] == 0:
            if kind == K:
                break
            ans += d
            cnt[t] += 1
            kind += 1
            ans += 2*kind-1
    print(ans)

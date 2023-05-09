def main():
    N, K = map(int, input().split())
    S = [list(map(int, input().split())) for _ in range(N)]
    S.sort(key=lambda x: x[1], reverse=True)
    ans = 0
    for i in range(K):
        ans += S[i][1]
    ans += K**2
    cnt = K
    kind = set()
    for i in range(K):
        kind.add(S[i][0])
    for i in range(K, N):
        if S[i][0] not in kind:
            if cnt >= K:
                continue
            cnt += 1
            kind.add(S[i][0])
            ans += S[i][1] - S[K - 1][1]
            ans += 2 * cnt - K - 1
    print(ans)

if __name__ == '__main__':
    main()
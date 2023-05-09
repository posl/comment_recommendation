def main():
    N, K = map(int, input().split())
    S = [input() for _ in range(N)]
    # 2^K通りの組み合わせを全探索
    ans = 0
    for i in range(1 << N):
        t = set()
        for j in range(N):
            if (i >> j) & 1:
                t |= set(S[j])
        if len(t) == K:
            ans += 1
    print(ans)

if __name__ == '__main__':
    main()
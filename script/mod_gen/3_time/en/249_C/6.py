def main():
    N, K = map(int, input().split())
    S = [input() for _ in range(N)]
    ans = 0
    for i in range(1 << N):
        if bin(i).count("1") != K:
            continue
        s = set()
        for j in range(N):
            if i >> j & 1:
                s |= set(S[j])
        ans = max(ans, len(s))
    print(ans)

if __name__ == '__main__':
    main()
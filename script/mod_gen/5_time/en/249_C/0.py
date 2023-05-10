def main():
    N, K = map(int, input().split())
    S = []
    for i in range(N):
        S.append(set(input()))
    ans = 0
    for i in range(1, 2 ** N):
        if bin(i).count("1") == K:
            tmp = set()
            for j in range(N):
                if (i >> j) & 1:
                    tmp |= S[j]
            ans = max(ans, len(tmp))
    print(ans)

if __name__ == '__main__':
    main()
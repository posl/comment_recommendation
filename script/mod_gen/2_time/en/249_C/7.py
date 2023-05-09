def main():
    N, K = map(int, input().split())
    S = [input() for _ in range(N)]
    ans = 0
    for i in range(2**N):
        num = 0
        tmp = set()
        for j in range(N):
            if (i >> j) & 1:
                num += 1
                for s in S[j]:
                    tmp.add(s)
        if num == K:
            ans = max(ans, len(tmp))
    print(ans)

if __name__ == '__main__':
    main()
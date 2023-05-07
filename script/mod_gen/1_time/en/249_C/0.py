def main():
    N, K = map(int, input().split())
    S = [input() for _ in range(N)]
    ans = 0
    for i in range(1 << 26):
        cnt = 0
        for s in S:
            for c in s:
                if (1 << (ord(c) - ord('a'))) & i:
                    cnt += 1
                    break
        if cnt >= K:
            ans = max(ans, bin(i).count('1'))
    print(ans)

if __name__ == '__main__':
    main()
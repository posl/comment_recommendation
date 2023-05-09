def main():
    N, K = map(int, input().split())
    S = [input() for i in range(N)]
    ans = 0
    for i in range(1 << 26):
        cnt = 0
        for j in range(N):
            cnt += all(i >> ord(s) & 1 for s in S[j])
        if cnt >= K:
            ans = max(ans, bin(i).count("1"))
    print(ans)

if __name__ == '__main__':
    main()
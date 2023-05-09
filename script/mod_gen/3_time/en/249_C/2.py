def main():
    N, K = map(int, input().split())
    S = [set(input()) for _ in range(N)]
    ans = 0
    for i in range(1 << 26):
        cnt = 0
        for j in range(N):
            if len(S[j] & set(chr(ord('a') + k) for k in range(26) if i >> k & 1)) >= K:
                cnt += 1
        ans = max(ans, cnt)
    print(ans)

if __name__ == '__main__':
    main()
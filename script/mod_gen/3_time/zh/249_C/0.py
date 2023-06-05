def main():
    N, K = map(int, input().split())
    S = [input() for _ in range(N)]
    ans = 0
    for i in range(1 << N):
        if bin(i).count("1") != K:
            continue
        cnt = 0
        for j in range(N):
            if i >> j & 1:
                cnt |= set(S[j])
        ans = max(ans, bin(cnt).count("1"))
    print(ans)

if __name__ == '__main__':
    main()
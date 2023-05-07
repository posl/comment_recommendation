def main():
    N, K = map(int, input().split())
    S = [input() for _ in range(N)]
    ans = 0
    for i in range(N):
        for j in range(i+1, N):
            cnt = 0
            for c in S[i]:
                if c in S[j]:
                    cnt += 1
            if cnt >= K:
                ans += 1
    print(ans)

if __name__ == '__main__':
    main()
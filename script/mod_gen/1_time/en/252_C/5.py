def main():
    N = int(input())
    S = [input() for _ in range(N)]
    S = [list(s) for s in S]
    ans = 0
    for i in range(10):
        cnt = [0]*10
        for j in range(N):
            cnt[int(S[j][i%10])] += 1
        ans += N - max(cnt)
    print(ans)

if __name__ == '__main__':
    main()
def main():
    N = int(input())
    S = [input() for _ in range(N)]
    ans = 0
    for i in range(10):
        cnt = [0] * 10
        for j in range(N):
            cnt[int(S[j][i % 10])] += 1
        ans += max(cnt) * 10 ** i
    print(ans)

if __name__ == '__main__':
    main()
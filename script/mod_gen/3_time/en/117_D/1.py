def main():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    ans = 0
    for i in range(60, -1, -1):
        cnt = 0
        for j in range(N):
            if A[j] & (1 << i):
                cnt += 1
        if cnt * 2 < N and K >= (1 << i):
            ans += cnt * (1 << i)
            K -= (1 << i)
        else:
            ans += (N - cnt) * (1 << i)
    print(ans)

if __name__ == '__main__':
    main()
def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    S = [0] * (N + 1)
    for i in range(N):
        S[i + 1] = (S[i] + A[i]) % M
    ans = 0
    cnt = [0] * M
    for i in range(N + 1):
        ans += cnt[S[i]]
        cnt[S[i]] += 1
    print(ans)

if __name__ == '__main__':
    main()
def main():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    S = [0] * (N + 1)
    for i in range(N):
        S[i + 1] = S[i] + A[i]
    from collections import defaultdict
    cnt = defaultdict(int)
    ans = 0
    for i in range(N + 1):
        ans += cnt[S[i]]
        cnt[S[i] + K] += 1
    print(ans)

if __name__ == '__main__':
    main()
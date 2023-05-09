def main():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    sumA = [0] * (N + 1)
    for i in range(N):
        sumA[i + 1] = sumA[i] + A[i]
    r = 0
    ans = 0
    for l in range(N):
        while r < N and sumA[r + 1] - sumA[l] < K:
            r += 1
        ans += N - r
    print(ans)

if __name__ == '__main__':
    main()
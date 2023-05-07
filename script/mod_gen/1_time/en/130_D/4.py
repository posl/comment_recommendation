def main():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    sumA = [0] * (N + 1)
    for i in range(N):
        sumA[i + 1] = sumA[i] + A[i]
    ans = 0
    r = 0
    for l in range(N):
        while r < N and sumA[r + 1] - sumA[l] < K:
            r += 1
        if r == N:
            break
        ans += N - r
    print(ans)

if __name__ == '__main__':
    main()
def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    B = [0] * (N + 1)
    for i in range(N):
        B[i + 1] = B[i] + A[i]
    ans = 0
    for i in range(N - M + 1):
        ans = max(ans, B[i + M] - B[i] + (M - 1) * A[i])
    print(ans)

if __name__ == '__main__':
    main()
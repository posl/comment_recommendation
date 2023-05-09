def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    A.sort()
    B = [0] * (N + 1)
    for i in range(N):
        B[i + 1] = B[i] + A[i]
    ans = 0
    for i in range(N):
        ans += A[i] * 2 ** min(M, i)
    print(ans - B[N])

if __name__ == '__main__':
    main()
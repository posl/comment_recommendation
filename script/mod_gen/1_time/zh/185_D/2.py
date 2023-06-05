def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    A.sort()
    if M == 0:
        print(1)
        return
    if N == M:
        print(0)
        return
    B = [0] * (M + 1)
    B[0] = A[0] - 1
    for i in range(1, M):
        B[i] = A[i] - A[i-1] - 1
    B[M] = N - A[M-1]
    B.sort()
    k = B[0]
    ans = 0
    for i in range(1, M + 1):
        ans += (B[i] + k - 1) // k
    print(ans)

if __name__ == '__main__':
    main()
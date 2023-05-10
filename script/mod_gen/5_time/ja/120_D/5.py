def main():
    N, M = map(int, input().split())
    A = [0] * M
    B = [0] * M
    for i in range(M):
        A[i], B[i] = map(int, input().split())
    ans = [0] * M
    ans[M-1] = N * (N - 1) // 2
    for i in range(M-1, 0, -1):
        if (A[i] < B[i]):
            ans[i-1] = ans[i] - (N - B[i]) * A[i]
            N -= 1
        else:
            ans[i-1] = ans[i] - (N - A[i]) * B[i]
            N -= 1
    for i in range(M):
        print(ans[i])

if __name__ == '__main__':
    main()
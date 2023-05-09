def main():
    N, K = map(int, input().split())
    A = [[int(i) for i in input().split()] for j in range(N)]
    B = [0] * (N * N)
    cnt = 0
    for i in range(N):
        for j in range(N):
            B[cnt] = A[i][j]
            cnt += 1
    B.sort()
    l = 0
    r = N * N
    while l + 1 < r:
        mid = (l + r) // 2
        if check(A, B[mid], N, K):
            r = mid
        else:
            l = mid
    print(B[r])

if __name__ == '__main__':
    main()
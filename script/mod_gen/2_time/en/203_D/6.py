def main():
    N, K = map(int, input().split())
    A = [list(map(int, input().split())) for _ in range(N)]
    A.sort()
    B = [A[i][j] for i in range(N) for j in range(N)]
    B.sort()
    left = 0
    right = N * N - 1
    while left < right:
        mid = (left + right) // 2
        count = 0
        for i in range(N):
            count += bisect.bisect_right(A[i], B[mid])
        if count < K * K // 2 + 1:
            left = mid + 1
        else:
            right = mid
    print(B[left])
main()

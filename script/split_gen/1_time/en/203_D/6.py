def main():
    N, K = map(int, input().split())
    A = []
    for i in range(N):
        A.append(list(map(int, input().split())))
    A.sort()
    A = [A[i][j] for i in range(N) for j in range(N)]
    left = 0
    right = N*N
    while right - left > 1:
        mid = (left + right) // 2
        if check(A, mid, N, K):
            right = mid
        else:
            left = mid
    print(right)

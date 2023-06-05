def solve():
    N, P, Q, R = map(int, input().split())
    A = list(map(int, input().split()))
    # A = [1, 3, 2, 2, 2, 3, 1, 4, 3, 2]
    # N, P, Q, R = 10, 5, 7, 5
    # N, P, Q, R = 9, 100, 101, 100
    # A = [31, 41, 59, 26, 53, 58, 97, 93, 23]
    # N, P, Q, R = 7, 1, 1, 1
    # A = [1, 1, 1, 1, 1, 1, 1]
    # 从左往右扫描，记录每个位置之前的最大值
    max_left = [0] * N
    max_left[0] = A[0]
    for i in range(1, N):
        max_left[i] = max(max_left[i - 1], A[i])
    # 从右往左扫描，记录每个位置之后的最大值
    max_right = [0] * N
    max_right[N - 1] = A[N - 1]
    for i in range(N - 2, -1, -1):
        max_right[i] = max(max_right[i + 1], A[i])
    # 从左往右扫描，记录每个位置之前的最小值
    min_left = [0] * N
    min_left[0] = A[0]
    for i in range(1, N):
        min_left[i] = min(min_left[i - 1], A[i])
    # 从右往左扫描，记录每个位置之后的最小值
    min_right = [0] * N
    min_right[N - 1] = A[N - 1]
    for i in range(N - 2, -1, -1):
        min_right[i] = min(min_right[i + 1], A[i])
    # 从左往

if __name__ == '__main__':
    solve()
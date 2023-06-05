def main():
    N, K = map(int, input().split())
    A = [list(map(int, input().split())) for _ in range(N)]
    def check(x):
        # 长度为K的一维数组，其元素都大于等于x，是否存在
        # 一个K×K的区域，其元素都大于等于x
        B = [[0] * (N + 1) for _ in range(N + 1)]
        for i in range(N):
            for j in range(N):
                B[i + 1][j + 1] = B[i + 1][j] + B[i][j + 1] - B[i][j]
                if A[i][j] >= x:
                    B[i + 1][j + 1] += 1
        for i in range(N - K + 1):
            for j in range(N - K + 1):
                if B[i + K][j + K] - B[i][j + K] - B[i + K][j] + B[i][j] >= K * K // 2 + 1:
                    return True
        return False
    # 二分探索
    left = -1
    right = 10 ** 9 + 1
    while right - left > 1:
        mid = (left + right) // 2
        if check(mid):
            left = mid
        else:
            right = mid
    print(left)
main()

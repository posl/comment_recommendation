def solve():
    N, X = map(int, input().split())
    A = []
    for i in range(N):
        A.append(list(map(int, input().split())))
    # ここにプログラムを追記
    # print(N, X, A)
    # 1. 全探索
    # 2. 二分探索
    # 3. DP
    # 4. 素因数分解
    # 1. 全探索
    # def dfs(i, x):
    #     if i == N:
    #         return x == X
    #     for j in range(A[i][0]):
    #         if dfs(i + 1, x * A[i][j + 1]):
    #             return True
    #     return False
    # print('Yes' if dfs(0, 1) else 'No')
    # 2. 二分探索
    # def dfs(i, x):
    #     if i == N:
    #         return x == X
    #     for j in range(A[i][0]):
    #         if dfs(i + 1, x * A[i][j + 1]):
    #             return True
    #     return False
    # print('Yes' if dfs(0, 1) else 'No')
    # 3. DP
    # dp = [0] * (X + 1)
    # dp[1] = 1
    # for i in range(N):
    #     for j in range(X, 0, -1):
    #         if dp[j] == 1:
    #             for k in range(A[i][0]):
    #                 dp[j * A[i][k + 1]] = 1
    # print('Yes' if dp[X] else 'No')
    # 4. 素因数分解
    # print(N, X, A)
    # for i in range(N):
    #     print(A[i][0])
    #     for j in range(A[i][0]):
    #         print(A[i][j + 1])
    # print('Yes' if dfs(0, 1) else 'No')
    # 5. 素因数分

if __name__ == '__main__':
    solve()
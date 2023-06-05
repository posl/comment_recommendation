def main():
    # 读入数据
    N = int(input())
    X, Y = map(int, input().split())
    A = []
    B = []
    for _ in range(N):
        a, b = map(int, input().split())
        A.append(a)
        B.append(b)
    # 初始化dp
    dp = [[False for _ in range(Y+1)] for _ in range(X+1)]
    dp[0][0] = True
    # 动态规划
    for i in range(N):
        for j in range(X, -1, -1):
            for k in range(Y, -1, -1):
                if not dp[j][k]:
                    continue
                if j + A[i] <= X and k + B[i] <= Y:
                    dp[j+A[i]][k+B[i]] = True
    # 输出结果
    if dp[X][Y]:
        print(sum(dp[X]))
    else:
        print(-1)

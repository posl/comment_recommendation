def main():
    # 读入
    N, M, C = map(int, input().split())
    B = list(map(int, input().split()))
    A = [list(map(int, input().split())) for i in range(N)]
    # 计算
    ans = 0
    for i in range(N):
        tmp = 0
        for j in range(M):
            tmp += A[i][j] * B[j]
        if tmp + C > 0:
            ans += 1
    # 输出
    print(ans)

def solve():
    # 输入
    N, M, C = map(int, input().split())
    B = list(map(int, input().split()))
    A = [list(map(int, input().split())) for _ in range(N)]
    # 计算
    ans = 0
    for i in range(N):
        if sum([A[i][j]*B[j] for j in range(M)]) + C > 0:
            ans += 1
    # 输出
    print(ans)
solve()

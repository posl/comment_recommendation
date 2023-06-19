def solve():
    # 读取输入
    N, X = map(int, input().split())
    A = []
    B = []
    for i in range(N):
        a, b = map(int, input().split())
        A.append(a)
        B.append(b)
    # 算法
    for i in range(N):
        X -= A[i] * B[i]
    if X < 0:
        print("No")
    else:
        print("Yes")
solve()

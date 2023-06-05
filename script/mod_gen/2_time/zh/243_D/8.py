def solution():
    N = int(input())
    X = []
    Y = []
    for i in range(N):
        x, y = map(int, input().split())
        X.append(x)
        Y.append(y)
    S = input()
    #print(X)
    #print(Y)
    #print(S)
    # 1. 按照S的方向，计算每个人的终点坐标
    X_end = [0] * N
    Y_end = [0] * N
    for i in range(N):
        if S[i] == 'R':
            X_end[i] = X[i] + 1
            Y_end[i] = Y[i]
        elif S[i] == 'L':
            X_end[i] = X[i] - 1
            Y_end[i] = Y[i]
        elif S[i] == 'U':
            X_end[i] = X[i]
            Y_end[i] = Y[i] + 1
        elif S[i] == 'D':
            X_end[i] = X[i]
            Y_end[i] = Y[i] - 1
    #print(X_end)
    #print(Y_end)
    # 2. 按照X坐标排序
    X_sorted = sorted(X_end)
    #print(X_sorted)
    # 3. 按照X坐标排序后，计算相邻两个人之间的距离
    # 3.1 计算相邻两个人之间的距离
    D = []
    for i in range(N-1):
        D.append(X_sorted[i+1] - X_sorted[i])
    #print(D)
    # 3.2 检查是否有人之间的距离为0
    for i in range(N-1):
        if D[i] == 0:
            print("Yes")
            return
    print("No")

if __name__ == '__main__':
    solution()
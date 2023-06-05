def main():
    N = int(input())
    X = []
    Y = []
    for i in range(N):
        x, y = map(int, input().split())
        X.append(x)
        Y.append(y)
    S = input()
    #print(N)
    #print(X)
    #print(Y)
    #print(S)
    # 1. 确定X轴上的人的初始位置
    # 2. 确定X轴上的人的初始方向
    # 3. 确定X轴上的人的移动规则
    # 4. 确定X轴上的人的移动规则
    # 5. 确定X轴上的人的移动规则
    # 6. 确定X轴上的人的移动规则
    # 7. 确定X轴上的人的移动规则
    # 8. 确定X轴上的人的移动规则
    # 9. 确定X轴上的人的移动规则
    # 10. 确定X轴上的人的移动规则
    # 1. 确定X轴上的人的初始位置
    X0 = []
    for i in range(N):
        if S[i] == 'R':
            X0.append(X[i])
        else:
            X0.append(-X[i])
    #print(X0)
    # 2. 确定X轴上的人的初始方向
    D0 = []
    for i in range(N):
        if S[i] == 'R':
            D0.append(1)
        else:
            D0.append(-1)
    #print(D0)
    # 3. 确定X轴上的人的移动规则
    # 4. 确定X轴上的人的移动规则
    # 5. 确定X轴上的人的移动规则
    # 6. 确定X轴上的人的移动规则
    # 7.

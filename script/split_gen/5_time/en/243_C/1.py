def solve():
    N = int(input())
    X = []
    Y = []
    for i in range(N):
        x, y = map(int, input().split())
        X.append(x)
        Y.append(y)
    S = input()
    #print(N, X, Y, S)
    X0 = []
    Y0 = []
    X1 = []
    Y1 = []
    for i in range(N):
        if S[i] == 'R':
            X0.append(X[i])
            Y0.append(Y[i])
        else:
            X1.append(X[i])
            Y1.append(Y[i])
    #print(X0, Y0, X1, Y1)
    if len(X0) == 0 or len(X1) == 0:
        print('No')
        return
    X0min = min(X0)
    X0max = max(X0)
    Y0min = min(Y0)
    Y0max = max(Y0)
    X1min = min(X1)
    X1max = max(X1)
    Y1min = min(Y1)
    Y1max = max(Y1)
    #print(X0min, X0max, Y0min, Y0max, X1min, X1max, Y1min, Y1max)
    if X0max < X1min or X1max < X0min or Y0max < Y1min or Y1max < Y0min:
        print('No')
    else:
        print('Yes')

def solve():
    N = int(input())
    X = []
    Y = []
    for i in range(N):
        x, y = map(int, input().split())
        X.append(x)
        Y.append(y)
    S = input()
    for i in range(N):
        if S[i] == 'R':
            X[i] += 1
        elif S[i] == 'L':
            X[i] -= 1
    for i in range(N):
        for j in range(i + 1, N):
            if X[i] == X[j] and Y[i] == Y[j]:
                print('Yes')
                return
    print('No')
    return

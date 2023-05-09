def main():
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
    for i in range(N):
        if S[i] == 'R':
            for j in range(N):
                if X[i] < X[j] and Y[i] == Y[j]:
                    print('Yes')
                    return
        if S[i] == 'L':
            for j in range(N):
                if X[i] > X[j] and Y[i] == Y[j]:
                    print('Yes')
                    return
    print('No')
    return

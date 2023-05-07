def main():
    N = int(input())
    X = []
    Y = []
    S = []
    for i in range(N):
        x, y = map(int, input().split())
        X.append(x)
        Y.append(y)
    S = input()
    #print(X)
    #print(Y)
    #print(S)
    for i in range(N):
        for j in range(i+1, N):
            if X[i] == X[j]:
                if Y[i] > Y[j]:
                    Y[i], Y[j] = Y[j], Y[i]
                    S = S[:i] + S[i][::-1] + S[i+1:]
                    S = S[:j] + S[j][::-1] + S[j+1:]
    #print(X)
    #print(Y)
    #print(S)
    for i in range(N):
        for j in range(i+1, N):
            if Y[i] == Y[j]:
                if X[i] > X[j]:
                    X[i], X[j] = X[j], X[i]
                    S = S[:i] + S[i][::-1] + S[i+1:]
                    S = S[:j] + S[j][::-1] + S[j+1:]
    #print(X)
    #print(Y)
    #print(S)
    for i in range(N-1):
        if S[i] == 'R' and S[i+1] == 'L':
            if X[i] == X[i+1]:
                if Y[i] == Y[i+1]:
                    print('Yes')
                    return
    print('No')

if __name__ == '__main__':
    main()
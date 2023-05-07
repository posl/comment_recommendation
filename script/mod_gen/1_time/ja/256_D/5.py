def main():
    N = int(input())
    S = []
    for _ in range(N):
        L, R = map(int, input().split())
        S.append([L, R])
    S.sort()
    X = []
    Y = []
    for i in range(N):
        if i == 0:
            X.append(S[i][0])
            Y.append(S[i][1])
        else:
            if S[i][0] <= Y[-1]:
                Y[-1] = max(Y[-1], S[i][1])
            else:
                X.append(S[i][0])
                Y.append(S[i][1])
    for i in range(len(X)):
        print(X[i], Y[i])

if __name__ == '__main__':
    main()
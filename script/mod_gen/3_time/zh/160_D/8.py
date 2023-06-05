def findShortest(N, X, Y):
    #print("N = {0}, X = {1}, Y = {2}".format(N, X, Y))
    if Y == X + 1:
        for i in range(1, N):
            print(i)
        return
    elif Y == N:
        for i in range(1, N):
            print(N - i)
        return
    elif Y < X + 1:
        for i in range(1, X):
            print(X - i + N - Y)
        return
    elif Y > N:
        for i in range(1, N):
            print(min(Y - i, i + N - Y))
        return
    else:
        for i in range(1, X):
            print(min(X - i + N - Y, Y - i))
        for i in range(X + 1, N):
            print(min(Y - X + i - 1, X - i + N - Y))
        return

if __name__ == '__main__':
    findShortest()
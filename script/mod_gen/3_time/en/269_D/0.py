def main():
    N = int(input())
    X = []
    Y = []
    for i in range(N):
        x, y = map(int, input().split())
        X.append(x)
        Y.append(y)
    X.sort()
    Y.sort()
    minx = X[0]
    miny = Y[0]
    maxx = X[N-1]
    maxy = Y[N-1]
    #print(minx, miny, maxx, maxy)
    #print(X, Y)
    #print(X[0], X[N-1], Y[0], Y[N-1])
    #print(X[0]-1, X[N-1]+1, Y[0]-1, Y[N-1]+1)
    #print(X[0]-1, X[N-1]+1, Y[0]-1, Y[N-1]+1)
    #print(X[0]-1, X[N-1]+1, Y[0]-1, Y[N-1]+1)
    #print(X[0]-1, X[N-1]+1, Y[0]-1, Y[N-1]+1)
    #print(X[0]-1, X[N-1]+1, Y[0]-1, Y[N-1]+1)
    #print(X[0]-1, X[N-1]+1, Y[0]-1, Y[N-1]+1)
    #print(X[0]-1, X[N-1]+1, Y[0]-1, Y[N-1]+1)
    #print(X[0]-1, X[N-1]+1, Y[0]-1, Y[N-1]+1)
    #print(X[0]-1, X[N-1]+1, Y[0]-1, Y[N-1]+1)
    #print(X[0]-1, X[N-1]+1, Y[0]-1, Y[N-1]+1)
    print(maxx-minx+1+maxy-miny+1-2)

if __name__ == '__main__':
    main()
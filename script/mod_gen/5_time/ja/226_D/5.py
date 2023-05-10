def main():
    N = int(input())
    X = []
    Y = []
    for i in range(N):
        x, y = map(int, input().split())
        X.append(x)
        Y.append(y)
    #print(X)
    #print(Y)
    ans = 0
    for i in range(N):
        for j in range(i+1, N):
            #print(i, j)
            if X[i] == X[j]:
                ans += 1
            elif Y[i] == Y[j]:
                ans += 1
            elif abs(X[i]-X[j]) == abs(Y[i]-Y[j]):
                ans += 1
    print(ans)

if __name__ == '__main__':
    main()
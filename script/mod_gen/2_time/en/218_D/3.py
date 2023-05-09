def main():
    N = int(input())
    X = []
    Y = []
    for i in range(N):
        x,y = map(int, input().split())
        X.append(x)
        Y.append(y)
    X.sort()
    Y.sort()
    ans = 0
    for i in range(N-1):
        for j in range(i+1,N):
            x = X[j] - X[i]
            for k in range(N-1):
                for l in range(k+1,N):
                    y = Y[l] - Y[k]
                    if x*y == 0:
                        continue
                    if (X[i],Y[k]) in zip(X,Y) and (X[j],Y[l]) in zip(X,Y):
                        ans += 1
    print(ans)

if __name__ == '__main__':
    main()
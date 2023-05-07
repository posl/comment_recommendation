def main():
    N = int(input())
    X = []
    Y = []
    for i in range(N):
        x,y = map(int,input().split())
        X.append(x)
        Y.append(y)
    ans = 0
    for i in range(N):
        for j in range(i+1,N):
            for k in range(j+1,N):
                if X[i] == X[j] and X[i] == X[k]:
                    continue
                if Y[i] == Y[j] and Y[i] == Y[k]:
                    continue
                if (X[i]-X[j])*(Y[i]-Y[k]) == (Y[i]-Y[j])*(X[i]-X[k]):
                    continue
                ans += 1
    print(ans)

if __name__ == '__main__':
    main()
def main():
    N = int(input())
    X = []
    Y = []
    for i in range(N):
        x,y = map(int, input().split())
        X.append(x)
        Y.append(y)
    ans = 0
    for i in range(N):
        for j in range(i+1,N):
            if abs(X[i]-X[j]) <= 1 and abs(Y[i]-Y[j]) <= 1:
                ans += 1
    print(ans)
main()

if __name__ == '__main__':
    main()
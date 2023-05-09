def main():
    N = int(input())
    X = []
    Y = []
    for i in range(N):
        x, y = map(int, input().split())
        X.append(x)
        Y.append(y)
    ans = 0
    for i in range(N):
        for j in range(i+1, N):
            ans = max(ans, ((X[i]-X[j])**2+(Y[i]-Y[j])**2)**0.5)
    print(ans)

if __name__ == '__main__':
    main()
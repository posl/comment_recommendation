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
    ans = 0
    for i in range(N):
        for j in range(i+1, N):
            for k in range(j+1, N):
                for l in range(k+1, N):
                    if (X[i] == X[j] and Y[k] == Y[l] and X[k] == X[l] and Y[i] == Y[j]) or (X[i] == X[k] and Y[j] == Y[l] and X[j] == X[l] and Y[i] == Y[k]) or (X[i] == X[l] and Y[j] == Y[k] and X[j] == X[k] and Y[i] == Y[l]):
                        ans += 1
    print(ans)

if __name__ == '__main__':
    main()
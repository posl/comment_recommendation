def main():
    N = int(input())
    X = []
    Y = []
    for i in range(N):
        x, y = map(int, input().split())
        X.append(x)
        Y.append(y)
    X = list(set(X))
    Y = list(set(Y))
    X.sort()
    Y.sort()
    ans = 0
    for i in range(len(X)):
        for j in range(i+1, len(X)):
            for k in range(len(Y)):
                for l in range(k+1, len(Y)):
                    cnt = 0
                    for m in range(N):
                        if X[i] <= X[m] <= X[j] and Y[k] <= Y[m] <= Y[l]:
                            cnt += 1
                    if cnt == 4:
                        ans += 1
    print(ans)

if __name__ == '__main__':
    main()
def main():
    N = int(input())
    X = []
    Y = []
    for _ in range(N):
        x, y = map(int, input().split())
        X.append(x)
        Y.append(y)
    X.sort()
    Y.sort()
    ans = 0
    for i in range(N):
        for j in range(i+1, N):
            for k in range(N):
                for l in range(k+1, N):
                    if X[i] <= X[k] and X[k] < X[j] and X[j] < X[l] and Y[k] <= Y[i] and Y[i] < Y[l] and Y[l] < Y[j]:
                        ans += 1
    print(ans)

if __name__ == '__main__':
    main()
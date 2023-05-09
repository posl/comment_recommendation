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
            for k in range(j+1, N):
                x1, y1 = X[i], Y[i]
                x2, y2 = X[j], Y[j]
                x3, y3 = X[k], Y[k]
                if x1*(y2-y3)+x2*(y3-y1)+x3*(y1-y2) == 0:
                    ans += 1
    print(ans)
main()

if __name__ == '__main__':
    main()
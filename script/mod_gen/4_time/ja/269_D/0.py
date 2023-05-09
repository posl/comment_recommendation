def main():
    N = int(input())
    X = [0] * N
    Y = [0] * N
    for i in range(N):
        X[i], Y[i] = map(int, input().split())
    ans = 0
    for i in range(N):
        for j in range(i+1, N):
            for k in range(j+1, N):
                x1, y1 = X[i], Y[i]
                x2, y2 = X[j], Y[j]
                x3, y3 = X[k], Y[k]
                if (y1 - y2) * (x1 - x3) == (y1 - y3) * (x1 - x2):
                    continue
                ans += 1
    print(ans)

if __name__ == '__main__':
    main()
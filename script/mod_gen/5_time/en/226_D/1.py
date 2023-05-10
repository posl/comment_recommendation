def main():
    N = int(input())
    x = []
    y = []
    for i in range(N):
        xi, yi = map(int, input().split())
        x.append(xi)
        y.append(yi)
    ans = 0
    for i in range(N):
        for j in range(i+1,N):
            x1 = x[j] - x[i]
            y1 = y[j] - y[i]
            ans = max(ans, (x1**2 + y1**2)**0.5)
    print(ans)

if __name__ == '__main__':
    main()
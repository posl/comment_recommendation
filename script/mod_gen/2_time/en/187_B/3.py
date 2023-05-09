def main():
    n = int(input())
    x = []
    y = []
    for i in range(n):
        xi, yi = map(int, input().split())
        x.append(xi)
        y.append(yi)
    ans = 0
    for i in range(n):
        for j in range(i + 1, n):
            if x[i] == x[j]:
                continue
            if -1 <= (y[i] - y[j]) / (x[i] - x[j]) <= 1:
                ans += 1
    print(ans)

if __name__ == '__main__':
    main()
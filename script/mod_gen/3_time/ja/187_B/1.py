def main():
    n = int(input())
    x = []
    y = []
    for i in range(n):
        x_i, y_i = map(int, input().split())
        x.append(x_i)
        y.append(y_i)
    ans = 0
    for i in range(n):
        for j in range(i+1, n):
            if -1 <= (y[j] - y[i]) / (x[j] - x[i]) <= 1:
                ans += 1
    print(ans)

if __name__ == '__main__':
    main()
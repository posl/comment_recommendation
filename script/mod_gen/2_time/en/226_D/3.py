def main():
    N = int(input())
    x = []
    y = []
    for i in range(N):
        x_i, y_i = map(int, input().split())
        x.append(x_i)
        y.append(y_i)
    ans = 0
    for i in range(N):
        for j in range(i):
            a = x[i] - x[j]
            b = y[i] - y[j]
            a2 = x[j] - x[i]
            b2 = y[j] - y[i]
            count = 0
            for k in range(N):
                if x[k] == x[i] + a and y[k] == y[i] + b:
                    count += 1
                if x[k] == x[i] + a2 and y[k] == y[i] + b2:
                    count += 1
            ans = max(ans, count)
    print(N - ans)

if __name__ == '__main__':
    main()
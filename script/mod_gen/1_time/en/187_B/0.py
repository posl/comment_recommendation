def main():
    N = int(input())
    x = []
    y = []
    for i in range(N):
        x_i, y_i = map(int, input().split())
        x.append(x_i)
        y.append(y_i)
    count = 0
    for i in range(N):
        for j in range(i + 1, N):
            if (y[i] - y[j]) / (x[i] - x[j]) <= 1 and (y[i] - y[j]) / (x[i] - x[j]) >= -1:
                count += 1
    print(count)

if __name__ == '__main__':
    main()
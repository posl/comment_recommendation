def main():
    N = int(input())
    x = []
    y = []
    for i in range(N):
        x_i, y_i = map(int, input().split())
        x.append(x_i)
        y.append(y_i)
    max_length = 0
    for i in range(N):
        for j in range(i + 1, N):
            length = ((x[i] - x[j]) ** 2 + (y[i] - y[j]) ** 2) ** 0.5
            if length > max_length:
                max_length = length
    print(max_length)

if __name__ == '__main__':
    main()
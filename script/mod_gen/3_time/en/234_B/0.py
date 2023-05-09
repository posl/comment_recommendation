def main():
    n = int(input())
    x = []
    y = []
    for i in range(n):
        x_i, y_i = map(int, input().split())
        x.append(x_i)
        y.append(y_i)
    max = 0
    for i in range(n):
        for j in range(i+1, n):
            distance = ((x[i] - x[j]) ** 2 + (y[i] - y[j]) ** 2) ** 0.5
            if distance > max:
                max = distance
    print(max)

if __name__ == '__main__':
    main()
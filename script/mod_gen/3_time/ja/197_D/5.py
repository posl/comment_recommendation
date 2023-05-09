def main():
    N = int(input())
    x_0, y_0 = map(int, input().split())
    x_N2, y_N2 = map(int, input().split())
    x_1 = (x_0 + x_N2) / 2 + (y_0 - y_N2) * (N / 4)**0.5
    y_1 = (y_0 + y_N2) / 2 + (x_N2 - x_0) * (N / 4)**0.5
    print(x_1, y_1)

if __name__ == '__main__':
    main()
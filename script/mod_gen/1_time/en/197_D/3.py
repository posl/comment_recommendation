def main():
    N = int(input())
    x_0, y_0 = map(int, input().split())
    x_N_2, y_N_2 = map(int, input().split())
    x_1 = (x_0 + x_N_2) / 2 - (y_0 - y_N_2) / (N / 2)
    y_1 = (y_0 + y_N_2) / 2 + (x_0 - x_N_2) / (N / 2)
    print(x_1, y_1)
main()

if __name__ == '__main__':
    main()
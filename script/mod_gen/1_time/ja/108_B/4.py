def main():
    x_1, y_1, x_2, y_2 = map(int, input().split())
    x_3 = x_2 + (y_1 - y_2)
    y_3 = y_2 - (x_1 - x_2)
    x_4 = x_3 + (x_1 - x_2)
    y_4 = y_3 + (y_1 - y_2)
    print(x_3, y_3, x_4, y_4)

if __name__ == '__main__':
    main()
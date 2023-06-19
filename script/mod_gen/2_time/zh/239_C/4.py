def main():
    x_1, y_1, x_2, y_2 = map(int, input().split())
    if (x_1-x_2)**2 + (y_1-y_2)**2 == 5:
        print("Yes")
    else:
        print("No")

if __name__ == '__main__':
    main()
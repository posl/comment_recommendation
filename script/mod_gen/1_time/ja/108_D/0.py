def main():
    L = int(input())
    if L == 2:
        print(4, 4)
        print(1, 2, 0)
        print(1, 3, 1)
        print(2, 4, 0)
        print(3, 4, 0)
    elif L == 3:
        print(4, 5)
        print(1, 2, 0)
        print(2, 3, 0)
        print(3, 4, 0)
        print(1, 3, 1)
        print(3, 4, 1)
    elif L == 4:
        print(8, 10)
        print(1, 2, 0)
        print(2, 3, 0)
        print(3, 4, 0)
        print(1, 5, 0)
        print(2, 6, 0)
        print(3, 7, 0)
        print(4, 8, 0)
        print(5, 6, 1)
        print(6, 7, 1)
        print(7, 8, 1)
    else:
        print(3 * L - 2, 3 * L - 3)
        for i in range(L - 1):
            print(i + 1, i + 2, 0)
        for i in range(L - 2):
            print(i + 1, i + 3, 1)
        print(1, 2 * L - 2, L - 1)
        print(2 * L - 3, 3 * L - 3, L - 1)

if __name__ == '__main__':
    main()
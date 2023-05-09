def main():
    L = int(input())
    if L % 2 == 0:
        print(2 * L, L)
        for i in range(1, L + 1):
            print(i, i + 1, 0)
            print(i, i + 1, 1)
    else:
        print(2 * L + 1, L + 1)
        for i in range(1, L + 1):
            print(i, i + 1, 0)
            print(i, i + 1, 1)
        print(L + 1, L + 2, 0)

if __name__ == '__main__':
    main()
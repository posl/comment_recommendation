def main():
    L = int(input())
    N = 20
    M = 60
    print(N, M)
    for i in range(M):
        if i < L:
            print(i + 1, i + 2, 0)
        elif i < 2 * L:
            print(i - L + 1, i - L + 2, 1)
        elif i < 3 * L:
            print(i - 2 * L + 1, i - 2 * L + 2, 2)
        elif i < 4 * L:
            print(i - 3 * L + 1, i - 3 * L + 2, 3)
        else:
            print(1, 3, i - 3 * L + 1)

if __name__ == '__main__':
    main()
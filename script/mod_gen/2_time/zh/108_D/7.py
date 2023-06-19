def main():
    L = int(input())
    N = 2
    M = 2 * L + 1
    print(N, M)
    print(1, 2, 0)
    for i in range(1, L + 1):
        print(2 * i - 1, 2 * i + 1, 1)
        print(2 * i, 2 * i + 1, 0)

if __name__ == '__main__':
    main()
def main():
    L = int(input())
    if L == 2:
        print(2, 1)
        print(1, 2, 1)
        return
    if L == 3:
        print(3, 2)
        print(1, 2, 2)
        print(2, 3, 1)
        return
    N = 2
    M = 1
    while 2 ** N <= L:
        N += 1
    N += 1
    M += N - 2
    print(N, M)
    for i in range(1, N):
        print(i, i + 1, 0)
    L -= 2 ** (N - 2)
    for i in range(N - 2, 0, -1):
        if L >= 2 ** (i - 1):
            L -= 2 ** (i - 1)
            print(i + 1, N, 2 ** (i - 1))
    print(1, N, L)
main()

if __name__ == '__main__':
    main()
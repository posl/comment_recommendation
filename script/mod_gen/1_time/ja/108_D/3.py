def main():
    L = int(input())
    N = 20
    M = 60
    print(N, M)
    for i in range(1, N):
        print(i, i + 1, 0)
    for i in range(1, N):
        print(i, i + 1, 10 ** 6)
    for i in range(N - 1, 0, -1):
        if L <= 10 ** 6:
            print(i, N, L)
            L = 0
        else:
            print(i, N, 10 ** 6)
            L -= 10 ** 6

if __name__ == '__main__':
    main()
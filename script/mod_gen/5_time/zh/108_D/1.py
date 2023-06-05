def main():
    L = int(input())
    N = 1
    M = 0
    while L > 0:
        N += 1
        L //= 2
        M += 1
    print(N, M)
    for i in range(1, N):
        print(i, i + 1, 0)
        print(i, i + 1, 2 ** (i - 1))
    L = int(input())
    for i in range(M - 1):
        if L & (1 << i):
            print(i + 1, i + 2, 2 ** i)
    return

if __name__ == '__main__':
    main()
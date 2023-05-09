def main():
    L = int(input())
    N = 20
    M = 60
    print(N, M)
    for i in range(1, N):
        print(i, i + 1, 0)
    for i in range(1, N):
        print(i, i + 1, i)
    for i in range(1, N):
        for j in range(i + 2, N + 1):
            print(i, j, i * (j - i) + 1)
    for i in range(1, L + 1):
        print(i, i + 1, 0)

if __name__ == '__main__':
    main()
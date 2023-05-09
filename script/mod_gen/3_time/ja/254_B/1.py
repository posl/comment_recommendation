def main():
    N = int(input())
    a = [[1] * (i + 1) for i in range(N)]
    for i in range(2, N):
        for j in range(1, i):
            a[i][j] = a[i - 1][j - 1] + a[i - 1][j]
    for i in range(N):
        print(*a[i])

if __name__ == '__main__':
    main()
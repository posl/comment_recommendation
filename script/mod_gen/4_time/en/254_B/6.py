def main():
    n = int(input())
    a = [0] * n
    for i in range(n):
        a[i] = [0] * (i + 1)
        a[i][0] = 1
        a[i][i] = 1
    for i in range(1, n):
        for j in range(1, i):
            a[i][j] = a[i - 1][j - 1] + a[i - 1][j]
    for i in range(n):
        print(*a[i])

if __name__ == '__main__':
    main()
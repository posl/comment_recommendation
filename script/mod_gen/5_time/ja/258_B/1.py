def main():
    n = int(input())
    a = [list(map(int, input())) for _ in range(n)]
    ans = 0
    for i in range(n):
        for j in range(n):
            if i == 0 and j == 0:
                continue
            if i == 0:
                a[i][j] += a[i][j-1]
            elif j == 0:
                a[i][j] += a[i-1][j]
            else:
                a[i][j] += max(a[i][j-1], a[i-1][j])
    print(a[n-1][n-1])

if __name__ == '__main__':
    main()
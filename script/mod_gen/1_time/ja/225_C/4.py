def main():
    n, m = map(int, input().split())
    b = [list(map(int, input().split())) for _ in range(n)]
    a = [[(i - 1) * 7 + j for j in range(1, 8)] for i in range(1, 10 ** 100)]
    for i in range(n):
        for j in range(m):
            if b[i][j] != a[i][j]:
                print("No")
                return
    print("Yes")

if __name__ == '__main__':
    main()
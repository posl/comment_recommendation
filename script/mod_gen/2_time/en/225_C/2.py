def main():
    n, m = map(int, input().split())
    b = [list(map(int, input().split())) for _ in range(n)]
    for i in range(n):
        for j in range(m):
            b[i][j] -= i*7+j+1
    for i in range(n):
        for j in range(m):
            if b[i][j] < 0 or b[i][j] % 7 != 0:
                print("No")
                return
    print("Yes")

if __name__ == '__main__':
    main()
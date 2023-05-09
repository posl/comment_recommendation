def main():
    n, m = map(int, input().split())
    a = [list(input()) for _ in range(n)]
    cnt = 0
    for i in range(n):
        for j in range(m):
            if a[i][j] == "#":
                cnt += 1
    print(cnt)

if __name__ == '__main__':
    main()
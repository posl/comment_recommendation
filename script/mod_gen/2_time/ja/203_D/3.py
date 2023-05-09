def main():
    n, k = map(int, input().split())
    a = [list(map(int, input().split())) for _ in range(n)]
    ans = 10 ** 10
    for i in range(n - k + 1):
        for j in range(n - k + 1):
            tmp = []
            for x in range(i, i + k):
                for y in range(j, j + k):
                    tmp.append(a[x][y])
            tmp.sort()
            ans = min(ans, tmp[k * k // 2])
    print(ans)

if __name__ == '__main__':
    main()
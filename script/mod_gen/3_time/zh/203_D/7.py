def main():
    n, k = map(int, input().split())
    a = [list(map(int, input().split())) for _ in range(n)]
    ans = 10 ** 9
    for i in range(n - k + 1):
        for j in range(n - k + 1):
            b = []
            for l in range(k):
                for m in range(k):
                    b.append(a[i + l][j + m])
            b.sort()
            ans = min(ans, b[(k * k) // 2])
    print(ans)

if __name__ == '__main__':
    main()
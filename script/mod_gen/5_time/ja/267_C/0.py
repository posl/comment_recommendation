def main():
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    ans = 0
    for i in range(n - m + 1):
        tmp = 0
        for j in range(m):
            tmp += (j + 1) * a[i + j]
        ans = max(ans, tmp)
    print(ans)

if __name__ == '__main__':
    main()
def main():
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    ans = -10000000000
    for i in range(n):
        for j in range(i, n):
            b = a[i:j+1]
            sorted(b)
            tmp = 0
            for k in range(len(b)):
                tmp += (k + 1) * b[k]
            ans = max(ans, tmp)
    print(ans)

if __name__ == '__main__':
    main()
def main():
    n = int(input())
    a = [int(x) for x in input().split()]
    d = {}
    for i in range(n):
        if a[i] in d:
            d[a[i]] += 1
        else:
            d[a[i]] = 1
    ans = 0
    for i in d:
        ans += d[i] * (d[i] - 1) // 2
    for i in range(n):
        print(ans - d[a[i]] + 1)
main()

if __name__ == '__main__':
    main()
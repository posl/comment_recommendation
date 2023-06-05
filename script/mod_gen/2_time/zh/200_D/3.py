def main():
    n = int(input())
    a = [int(i) for i in input().split()]
    d = {}
    for i in range(n):
        if a[i] % 200 in d:
            d[a[i] % 200] += 1
        else:
            d[a[i] % 200] = 1
    ans = 0
    for i in d:
        ans += d[i] * (d[i] - 1) // 2
    print(ans)

if __name__ == '__main__':
    main()
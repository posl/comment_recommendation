def main():
    n = int(input())
    a = list(map(int, input().split()))
    d = {}
    for i in a:
        if i in d:
            d[i] += 1
        else:
            d[i] = 1
    ans = 0
    for i in d.values():
        ans += i * (n - i)
    print(ans // 2)

if __name__ == '__main__':
    main()
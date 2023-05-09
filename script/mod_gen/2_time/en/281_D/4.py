def main():
    n, k, d = map(int, input().split())
    a = list(map(int, input().split()))
    s = set()
    for i in range(2**n):
        tmp = 0
        for j in range(n):
            if (i >> j) & 1:
                tmp += a[j]
        s.add(tmp)
    ans = -1
    for i in s:
        if i % d == 0:
            ans = max(ans, i)
    print(ans)

if __name__ == '__main__':
    main()
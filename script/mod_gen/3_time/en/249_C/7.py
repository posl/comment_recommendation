def main():
    n, k = map(int, input().split())
    s = [input() for _ in range(n)]
    ans = 0
    for i in range(2 ** n):
        t = []
        for j in range(n):
            if (i >> j) & 1:
                t.append(s[j])
        u = set()
        for x in t:
            for y in x:
                u.add(y)
        c = 0
        for x in u:
            if sum(x in y for y in t) == k:
                c += 1
        ans = max(ans, c)
    print(ans)

if __name__ == '__main__':
    main()
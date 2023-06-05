def main():
    n, m = map(int, input().split())
    d = {}
    for i in range(m):
        k, *a = map(int, input().split())
        for j in range(k):
            if a[j] not in d:
                d[a[j]] = set()
            d[a[j]].add(i)
    ans = 'Yes'
    for v in d.values():
        if len(v) == 1:
            ans = 'No'
            break
    print(ans)

if __name__ == '__main__':
    main()
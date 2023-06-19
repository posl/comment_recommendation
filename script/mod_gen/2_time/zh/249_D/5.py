def main():
    n = int(input())
    a = list(map(int, input().split()))
    cnt = 0
    d = {}
    for i in range(n):
        if a[i] not in d:
            d[a[i]] = 0
        d[a[i]] += 1
    for i in range(n):
        for j in range(n):
            if a[j] == 0:
                continue
            if a[i] % a[j] != 0:
                continue
            if a[i] // a[j] in d:
                cnt += d[a[i] // a[j]]
    print(cnt)

if __name__ == '__main__':
    main()
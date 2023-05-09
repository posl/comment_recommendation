def main():
    n = int(input())
    a = list(map(int, input().split()))
    ans = 0
    d = {}
    for i in range(n):
        if a[i] in d:
            d[a[i]] += 1
        else:
            d[a[i]] = 1
    for i in range(n):
        for j in range(n):
            if a[i] % a[j] == 0:
                if a[i] // a[j] in d:
                    ans += d[a[i] // a[j]]
    print(ans)

if __name__ == '__main__':
    main()
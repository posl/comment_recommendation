def main():
    n = int(input())
    a = list(map(lambda x: int(x) % 200, input().split()))
    a.sort()
    #print(a)
    d = {}
    for i in range(n):
        if a[i] in d:
            d[a[i]] += 1
        else:
            d[a[i]] = 1
    #print(d)
    ans = 0
    for k in d:
        if d[k] > 1:
            ans += int(d[k] * (d[k] - 1) / 2)
    print(ans)

if __name__ == '__main__':
    main()
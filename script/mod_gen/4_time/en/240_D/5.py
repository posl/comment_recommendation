def main():
    N = int(input())
    a = list(map(int, input().split()))
    d = {}
    d[0] = 1
    for i in range(N):
        if a[i] in d:
            d[a[i]] += 1
        else:
            d[a[i]] = 1
        if a[i]-1 in d:
            d[a[i]-1] += 1
        else:
            d[a[i]-1] = 1
        if a[i]+1 in d:
            d[a[i]+1] += 1
        else:
            d[a[i]+1] = 1
    print(max(d.values()))

if __name__ == '__main__':
    main()
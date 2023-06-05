def main():
    n = int(input())
    a = list(map(int, input().split()))
    a = [0] + a
    for i in range(1, n):
        a[i + 1] += a[i]
    for i in range(n):
        a[i + 1] %= 200
    d = {}
    for i in range(n + 1):
        if a[i] in d:
            d[a[i]].append(i)
        else:
            d[a[i]] = [i]
    for k, v in d.items():
        if len(v) > 1:
            print('Yes')
            print(1, v[0])
            print(1, v[1])
            return
    print('No')

if __name__ == '__main__':
    main()
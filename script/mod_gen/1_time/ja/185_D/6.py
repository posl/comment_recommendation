def main():
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    a.sort()
    a.append(n + 1)
    d = []
    for i in range(m + 1):
        d.append(a[i] - a[i - 1] - 1)
    d.sort()
    d = [i for i in d if i != 0]
    if len(d) == 0:
        print(0)
        return
    k = d[0]
    for i in range(1, len(d)):
        k = gcd(k, d[i])
    print((max(d) - 1) // k + 1)

if __name__ == '__main__':
    main()
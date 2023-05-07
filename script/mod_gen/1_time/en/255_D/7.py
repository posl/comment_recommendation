def main():
    n, q = map(int, input().split())
    a = list(map(int, input().split()))
    x = [int(input()) for _ in range(q)]
    a.sort()
    a.append(10**20)
    b = [0]
    for i in range(1, n + 1):
        b.append(b[i - 1] + a[i] - a[i - 1])
    for i in range(q):
        l = 0
        r = n
        while r - l > 1:
            m = (l + r) // 2
            if a[m] < x[i]:
                l = m
            else:
                r = m
        print(b[l] + (n - l) * (x[i] - 1))

if __name__ == '__main__':
    main()
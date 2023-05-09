def main():
    n, q = map(int, input().split())
    a = list(map(int, input().split()))
    x = [int(input()) for _ in range(q)]
    a.sort()
    for i in range(q):
        l, r = 0, n
        while r - l > 1:
            c = (l + r) // 2
            if a[c] >= x[i]:
                r = c
            else:
                l = c
        print(n - r)

if __name__ == '__main__':
    main()
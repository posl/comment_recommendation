def main():
    n, q = map(int, input().split())
    a = list(map(int, input().split()))
    x = [int(input()) for i in range(q)]
    a.sort()
    for i in range(q):
        l = 0
        r = n
        while r - l > 1:
            c = (r + l) // 2
            if a[c] <= x[i]:
                l = c
            else:
                r = c
        if a[l] > x[i]:
            print(l)
        else:
            print(l + 1)

if __name__ == '__main__':
    main()
def main():
    n, q = map(int, input().split())
    a = list(map(int, input().split()))
    x = []
    for i in range(q):
        x.append(int(input()))
    a.sort()
    for i in range(q):
        l = 0
        r = n-1
        while l <= r:
            m = (l+r)//2
            if a[m] >= x[i]:
                r = m-1
            else:
                l = m+1
        print(n-l)
main()

if __name__ == '__main__':
    main()
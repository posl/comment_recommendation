def main():
    n, p, q, r, s = map(int, input().split())
    a = list(map(int, input().split()))
    b = a[p-1:q] + a[r-1:s]
    b.sort()
    a[p-1:q] = b[:q-p]
    a[r-1:s] = b[q-p:]
    print(*a)

if __name__ == '__main__':
    main()
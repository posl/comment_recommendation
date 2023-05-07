def main():
    n, p, q, r, s = map(int, input().split())
    a = list(map(int, input().split()))
    b = a[:]
    b[p-1:q] = a[r-1:s]
    b[r-1:s] = a[p-1:q]
    print(*b)

if __name__ == '__main__':
    main()
def main():
    n, p, q, r, s = map(int, input().split())
    a = list(map(int, input().split()))
    b = a[:]
    b[p - 1:q] = a[q - 1:r - 1: -1]
    b[r - 1:s] = a[s - 1:p - 1: -1]
    print(*b)

if __name__ == '__main__':
    main()
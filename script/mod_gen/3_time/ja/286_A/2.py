def main():
    n, p, q, r, s = map(int, input().split())
    a = list(map(int, input().split()))
    b = a[p-1:q] + a[r-1:s]
    for i in range(n):
        if i < p-1 or s <= i:
            b.append(a[i])
    print(*b)

if __name__ == '__main__':
    main()
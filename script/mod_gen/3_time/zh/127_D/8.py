def main():
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    b = []
    c = []
    for i in range(m):
        b_i, c_i = map(int, input().split())
        b.append(b_i)
        c.append(c_i)
    a.sort()
    c.sort(reverse=True)
    i = 0
    j = 0
    while i < n and j < m:
        if a[i] < c[j]:
            a[i] = c[j]
            j += 1
        i += 1
    print(sum(a))

if __name__ == '__main__':
    main()
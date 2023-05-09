def main():
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    b = [0] * m
    c = [0] * m
    for i in range(m):
        b[i], c[i] = map(int, input().split())
    a.sort()
    c.sort()
    i = 0
    j = 0
    while i < n and j < m:
        if a[i] < c[j]:
            a[i] = c[j]
            b[j] -= 1
            if b[j] == 0:
                j += 1
        i += 1
    print(sum(a))

if __name__ == '__main__':
    main()
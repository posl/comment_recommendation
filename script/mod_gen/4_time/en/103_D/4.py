def main():
    n, m = map(int, input().split())
    a, b = [0] * m, [0] * m
    for i in range(m):
        a[i], b[i] = map(int, input().split())
        a[i] -= 1
        b[i] -= 1
    a.sort()
    b.sort()
    cnt = 0
    i, j = 0, 0
    while i < m and j < m:
        if a[i] <= b[j]:
            cnt += 1
            i += 1
        else:
            cnt -= 1
            j += 1
    print(cnt)

if __name__ == '__main__':
    main()
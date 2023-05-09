def main():
    n, k = map(int, input().split())
    p = list(map(int, input().split()))
    p = [0] + p
    a = [0] * (n + 1)
    b = [0] * (n + 1)
    c = [0] * (n + 1)
    for i in range(1, n + 1):
        a[i] = i - 1
        b[i] = i + 1
    s = []
    for i in range(1, n + 1):
        while len(s) > 0 and p[s[-1]] >= p[i]:
            s.pop()
        if len(s) == 0:
            c[i] = -1
        else:
            c[i] = s[-1]
        s.append(i)
    for i in range(1, n + 1):
        if c[i] == -1:
            continue
        if p[i] - p[c[i]] <= k:
            continue
        b[a[c[i]]] = b[i]
        a[b[i]] = a[c[i]]
    for i in range(1, n + 1):
        if a[i] == 0:
            continue
        if b[i] - a[i] - 1 >= k:
            continue
        a[b[i]] = a[i]
        b[a[i]] = b[i]
    for i in range(1, n + 1):
        if a[i] == 0:
            print(-1)
        else:
            print(b[i] - a[i] - 1)

if __name__ == '__main__':
    main()
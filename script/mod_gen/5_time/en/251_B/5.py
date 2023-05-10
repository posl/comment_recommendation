def main():
    n, w = map(int, input().split())
    a = list(map(int, input().split()))
    a.sort()
    a = a[:n]
    b = [0] * (w + 1)
    for i in a:
        b[i] += 1
    c = [0] * (w + 1)
    for i in range(1, w + 1):
        c[i] = c[i - 1] + b[i]
    ans = 0
    for i in range(n):
        for j in range(i, n):
            for k in range(j, n):
                if a[i] + a[j] + a[k] <= w:
                    ans += c[w - a[i] - a[j] - a[k]] - c[a[k]]
    print(ans)

if __name__ == '__main__':
    main()
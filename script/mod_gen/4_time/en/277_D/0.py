def main():
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    b = [0] * m
    for i in range(n):
        b[a[i]] += 1
    c = [0] * m
    for i in range(m):
        c[i] = (m + i - 1) % m
    for i in range(m - 1):
        if b[i] > 0 and b[i + 1] > 0:
            b[i] -= 1
            b[i + 1] -= 1
            b[c[i]] += 1
    ans = 0
    for i in range(m):
        ans += i * b[i]
    print(ans)

if __name__ == '__main__':
    main()
def main():
    n = int(input())
    p = list(map(int, input().split()))
    k = 0
    for i in range(n):
        k += p[i] * (n - i - 1)
    k -= 1
    q = [0] * n
    for i in range(n):
        q[i] = k // (n - i - 1)
        k %= n - i - 1
    for i in range(n):
        for j in range(i):
            if q[j] <= q[i]:
                q[i] += 1
    r = [0] * n
    for i in range(n):
        r[i] = i + 1
    for i in range(n):
        for j in range(i):
            if r[j] <= r[i]:
                r[i] += 1
    for i in range(n):
        r[i] = p[r[i] - 1]
    for i in range(n):
        r[i] = r[q[i]]
    print(*r)

if __name__ == '__main__':
    main()
def solve():
    n, m, k = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    for i in range(1, n):
        a[i] += a[i - 1]
    for i in range(1, m):
        b[i] += b[i - 1]
    result = 0
    for i in range(n):
        if a[i] > k:
            break
        result = i + 1
    for i in range(m):
        if b[i] > k:
            break
        result = max(result, i + 1)
    for i in range(n):
        if a[i] > k:
            break
        j = m - 1
        while j >= 0 and a[i] + b[j] > k:
            j -= 1
        result = max(result, i + 1 + j + 1)
    for i in range(m):
        if b[i] > k:
            break
        j = n - 1
        while j >= 0 and b[i] + a[j] > k:
            j -= 1
        result = max(result, i + 1 + j + 1)
    print(result)

if __name__ == '__main__':
    solve()
def main():
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    if m == 0:
        print(1)
        return
    a.sort()
    a = [0] + a + [n+1]
    b = [a[i+1] - a[i] - 1 for i in range(m+1)]
    b.sort(reverse=True)
    k = 0
    for i in range(m+1):
        if b[i] == 0:
            break
        if k == 0:
            k = b[i]
        else:
            k = gcd(k, b[i])
    print((n - sum(b)) // k + 1)

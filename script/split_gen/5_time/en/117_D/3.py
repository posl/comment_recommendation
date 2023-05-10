def main():
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    b = [0] * 41
    for i in range(41):
        for j in range(n):
            if a[j] >> i & 1:
                b[i] += 1
    c = 0
    for i in range(40, -1, -1):
        if c + 2 ** i <= k:
            if b[i] > n - b[i]:
                c += 2 ** i
        else:
            if b[i] <= n - b[i]:
                c += 2 ** i
    d = 0
    for i in range(n):
        d += c ^ a[i]
    print(d)

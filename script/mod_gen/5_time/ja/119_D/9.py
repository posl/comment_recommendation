def binary_search(a, x):
    l = 0
    r = len(a)
    while l < r:
        m = (l + r) // 2
        if x < a[m]:
            r = m
        else:
            l = m + 1
    return l
a, b, q = map(int, input().split())
s = [int(input()) for _ in range(a)]
t = [int(input()) for _ in range(b)]
x = [int(input()) for _ in range(q)]
for i in range(q):
    ans = 10**18
    sr = binary_search(s, x[i])
    tr = binary_search(t, x[i])
    for si in (sr-1, sr):
        for ti in (tr-1, tr):
            d1 = abs(s[si] - x[i]) + abs(t[ti] - s[si])
            d2 = abs(t[ti] - x[i]) + abs(s[si] - t[ti])
            ans = min(ans, d1, d2)
    print(ans)

if __name__ == '__main__':
    binary_search()
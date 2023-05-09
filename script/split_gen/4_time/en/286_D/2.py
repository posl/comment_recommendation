def main():
    n, x = map(int, input().split())
    a = []
    b = []
    for i in range(n):
        c, d = map(int, input().split())
        a.append(c)
        b.append(d)
    total = 0
    for i in range(n):
        total += a[i] * b[i]
    if total <= x:
        print('Yes')
    else:
        print('No')

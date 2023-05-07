def main():
    n, m, t = map(int, input().split())
    a = [0] * m
    b = [0] * m
    for i in range(m):
        a[i], b[i] = map(int, input().split())
    a.append(t)
    b.append(t)
    m += 1
    c = 0
    for i in range(m):
        if i == 0:
            c = n - a[i]
        else:
            c = c + b[i - 1] - a[i]
        if c <= 0:
            print('No')
            return
        c = min(c + a[i] - b[i - 1], n)
    print('Yes')

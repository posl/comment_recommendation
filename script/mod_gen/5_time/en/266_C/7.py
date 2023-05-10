def is_convex(a, b, c, d):
    a1 = (b[0] - a[0], b[1] - a[1])
    b1 = (c[0] - b[0], c[1] - b[1])
    c1 = (d[0] - c[0], d[1] - c[1])
    d1 = (a[0] - d[0], a[1] - d[1])
    return a1[0] * b1[1] - a1[1] * b1[0] > 0 and b1[0] * c1[1] - b1[1] * c1[0] > 0 and c1[0] * d1[1] - c1[1] * d1[0] > 0 and d1[0] * a1[1] - d1[1] * a1[0] > 0
a = list(map(int, input().split()))
b = list(map(int, input().split()))
c = list(map(int, input().split()))
d = list(map(int, input().split()))
print('Yes' if is_convex(a, b, c, d) else 'No')

if __name__ == '__main__':
    is_convex()
def main():
    n, x, y, z = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    c = []
    for i in range(n):
        c.append((a[i] + b[i], a[i], b[i], i + 1))
    c.sort(reverse=True)
    d = []
    for i in range(x):
        d.append(c[i][3])
    d.sort()
    print(*d, sep='\n')
    d = []
    for i in range(x, x + y):
        d.append(c[i][3])
    d.sort()
    print(*d, sep='\n')
    d = []
    for i in range(x + y, x + y + z):
        d.append(c[i][3])
    d.sort()
    print(*d, sep='\n')

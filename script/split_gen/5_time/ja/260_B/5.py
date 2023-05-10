def main():
    n, x, y, z = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    c = []
    for i in range(n):
        c.append((a[i], b[i], i + 1))
    c.sort(key=lambda x: x[2])
    c.sort(key=lambda x: x[1], reverse=True)
    c.sort(key=lambda x: x[0], reverse=True)
    for i in range(x):
        print(c[i][2])
    for i in range(y):
        print(c[i + x][2])
    for i in range(z):
        print(c[i + x + y][2])

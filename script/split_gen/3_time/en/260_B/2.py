def main():
    n, x, y, z = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    c = []
    for i in range(n):
        c.append([a[i], b[i], a[i] + b[i], i + 1])
    c.sort(key=lambda x: (x[0], -x[1], -x[2], x[3]), reverse=True)
    for i in range(x + y + z):
        if i < x:
            print(c[i][3])
        elif i < x + y:
            if c[i][0] != c[i - 1][0]:
                print(c[i][3])
        else:
            if c[i][0] != c[i - 1][0] and c[i][1] != c[i - 1][1]:
                print(c[i][3])

def problems260_b():
    n, x, y, z = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    c = []
    for i in range(n):
        c.append([i, a[i] + b[i]])
    c.sort(key=lambda x: x[1], reverse=True)
    c.sort(key=lambda x: x[0])
    for i in range(x + y + z):
        print(c[i][0] + 1)

if __name__ == '__main__':
    problems260_b()
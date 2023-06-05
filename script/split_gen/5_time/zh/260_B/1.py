def main():
    n, x, y, z = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    c = [(i, a[i], b[i], a[i] + b[i]) for i in range(n)]
    c.sort(key=lambda x: -x[3])
    c.sort(key=lambda x: -x[2])
    c.sort(key=lambda x: -x[1])
    c = c[:x + y + z]
    c.sort()
    for i in c:
        print(i[0] + 1)

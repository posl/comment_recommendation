def main():
    n, x, y, z = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    c = []
    for i in range(n):
        c.append((a[i], b[i], i+1))
    c.sort(key=lambda x: x[2])
    c.sort(key=lambda x: x[1], reverse=True)
    c.sort(key=lambda x: x[0], reverse=True)
    c = c[:x+y+z]
    c.sort(key=lambda x: x[2])
    for i in c:
        print(i[2])

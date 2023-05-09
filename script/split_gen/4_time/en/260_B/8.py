def main():
    n, x, y, z = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    c = [i for i in range(1, n+1)]
    d = list(zip(c, a, b))
    d.sort(key=lambda x: x[2], reverse=True)
    d.sort(key=lambda x: x[1], reverse=True)
    d.sort(key=lambda x: x[1]+x[2], reverse=True)
    for i in range(x+y+z):
        print(d[i][0])

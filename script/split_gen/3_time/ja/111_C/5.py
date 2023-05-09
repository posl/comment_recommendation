def main():
    n = int(input())
    v = list(map(int, input().split()))
    a = v[::2]
    b = v[1::2]
    c = sorted(a+b)
    d = c[0]
    e = c[1]
    f = a.count(d)
    g = b.count(d)
    h = a.count(e)
    i = b.count(e)
    j = max(f+g, h+i)
    print(n-j)

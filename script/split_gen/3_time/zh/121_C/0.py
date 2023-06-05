def main():
    n, m = map(int, input().split())
    a = []
    b = []
    for i in range(n):
        ai, bi = map(int, input().split())
        a.append(ai)
        b.append(bi)
    bsum = sum(b)
    if m <= bsum:
        print(sum([a[i]*b[i] for i in range(n) if m > 0]))
    else:
        print(sum([a[i]*b[i] for i in range(n)]) + a[b.index(min(b))]*(m-bsum))

def main():
    n, q = map(int, input().split())
    p = [i for i in range(n + 1)]
    r = [0 for i in range(n + 1)]
    for i in range(q):
        c, x, y = map(int, input().split())
        if c == 1:
            unite(p, r, x, y)
        elif c == 2:
            disconnect(p, r, x, y)
        else:
            print(size(p, x), end=' ')
            s = []
            while x != p[x]:
                s.append(x)
                x = p[x]
            for i in s:
                p[i] = x
            print(*s[::-1])

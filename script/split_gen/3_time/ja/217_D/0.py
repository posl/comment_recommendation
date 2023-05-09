def main():
    L, Q = map(int, input().split())
    l = [0, L]
    for i in range(Q):
        c, x = map(int, input().split())
        if c == 1:
            l.append(x)
        else:
            l.sort()
            print(l[bisect.bisect(l, x)] - l[bisect.bisect(l, x) - 1])

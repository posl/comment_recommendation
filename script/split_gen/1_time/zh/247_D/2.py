def main():
    import sys
    readline = sys.stdin.readline
    write = sys.stdout.write
    n = int(readline())
    a = []
    b = []
    for _ in range(n):
        q = readline().split()
        if q[0] == "1":
            x, c = int(q[1]), int(q[2])
            a.append((x, c))
        else:
            c = int(q[1])
            b.append(c)
    a.reverse()
    for c in b:
        s = 0
        while c > 0:
            if len(a) == 0:
                break
            x, d = a[-1]
            a.pop()
            if c >= d:
                s += x * d
                c -= d
            else:
                s += x * c
                a.append((x, d - c))
                break
        write("%d\n" % s)
    return
main()

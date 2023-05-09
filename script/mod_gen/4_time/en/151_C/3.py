def problem151_c():
    n, m = map(int, input().split())
    p = [0] * n
    s = [0] * n
    for i in range(m):
        pi, si = map(str, input().split())
        pi = int(pi)
        if s[pi-1] == 0:
            if si == 'AC':
                p[pi-1] = 1
            else:
                s[pi-1] += 1
        else:
            pass
    print(sum(p), sum(s))

if __name__ == '__main__':
    problem151_c()
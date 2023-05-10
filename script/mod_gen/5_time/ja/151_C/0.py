def problems151_c():
    n, m = map(int, input().split())
    p = [0] * n
    s = [0] * n
    for i in range(m):
        pi, si = input().split()
        pi = int(pi)
        if s[pi - 1] == 0:
            if si == "AC":
                p[pi - 1] += 1
            else:
                s[pi - 1] += 1
        else:
            continue
    print(sum(p), sum(s))

if __name__ == '__main__':
    problems151_c()
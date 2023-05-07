def main():
    n, m = map(int, input().split())
    p = [0] * n
    s = [0] * n
    for i in range(m):
        pi, si = map(str, input().split())
        pi = int(pi)
        if s[pi-1] == 0:
            if si == 'AC':
                p[pi-1] += 1
                s[pi-1] = 1
            else:
                p[pi-1] -= 1
        else:
            continue
    print(sum(s), sum(p))

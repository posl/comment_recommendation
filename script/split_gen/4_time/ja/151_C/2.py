def main():
    n, m = map(int, input().split())
    p = [0] * (n + 1)
    s = [0] * (n + 1)
    for i in range(m):
        pi, si = input().split()
        pi = int(pi)
        if s[pi] == 0:
            if si == "AC":
                p[pi] += 1
                s[pi] = 1
            else:
                p[pi] += 1
        else:
            pass
    print(sum(s), sum(p))

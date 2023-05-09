def main():
    n, m = map(int, input().split())
    p = [0] * n
    s = [0] * n
    for i in range(m):
        pi, si = input().split()
        p[int(pi) - 1] = 1
        if si == 'AC':
            s[int(pi) - 1] = 1
    print(sum(s), sum([p[i] * (1 - s[i]) for i in range(n)]))

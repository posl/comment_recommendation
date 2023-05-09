def main():
    n, m = map(int, input().split())
    p = [0] * n
    s = [''] * n
    for i in range(m):
        p[i], s[i] = input().split()
        p[i] = int(p[i])
    ac = [0] * n
    wa = [0] * n
    for i in range(m):
        if s[i] == 'AC':
            ac[p[i] - 1] = 1
        else:
            if ac[p[i] - 1] == 0:
                wa[p[i] - 1] += 1
    print(sum(ac), sum([ac[i] * wa[i] for i in range(n)]))

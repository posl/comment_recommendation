def main():
    N, M = map(int, input().split())
    p = [0 for _ in range(N + 1)]
    s = [0 for _ in range(N + 1)]
    for _ in range(M):
        pi, si = input().split()
        pi = int(pi)
        if s[pi] == 0:
            if si == 'AC':
                s[pi] = 1
            else:
                p[pi] += 1
    ac = sum(s)
    wa = 0
    for i in range(1, N + 1):
        if s[i] == 1:
            wa += p[i]
    print('{} {}'.format(ac, wa))

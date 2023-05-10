def main():
    n, m = map(int, input().split())
    p = [0] * n
    s = [0] * n
    for _ in range(m):
        pi, si = input().split()
        pi = int(pi) - 1
        if s[pi] == 0 and si == 'AC':
            s[pi] = 1
        elif s[pi] == 0 and si == 'WA':
            p[pi] += 1
    print(sum(s), sum([p[i] * s[i] for i in range(n)]))

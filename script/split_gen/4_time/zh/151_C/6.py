def main():
    n, m = map(int, input().split())
    p = [0] * n
    s = [0] * n
    for i in range(m):
        p_i, s_i = input().split()
        p_i = int(p_i) - 1
        if s[p_i] == 0:
            if s_i == 'AC':
                s[p_i] = 1
            else:
                p[p_i] += 1
    print(sum(s), sum([p[i] for i in range(n) if s[i] == 1]))

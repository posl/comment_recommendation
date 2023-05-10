def main():
    n, m = map(int, input().split())
    p = [0] * n
    s = [0] * n
    for i in range(m):
        p_, s_ = input().split()
        p_ = int(p_) - 1
        p[p_] += 1
        s[p_] = s_
    ac = 0
    wa = 0
    for i in range(n):
        if p[i] == 0:
            continue
        if s[i] == 'AC':
            ac += 1
            wa += p[i] - 1
    print(ac, wa)

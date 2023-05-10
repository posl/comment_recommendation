def main():
    n, m = map(int, input().split())
    p = []
    s = []
    for i in range(m):
        a, b = input().split()
        p.append(int(a))
        s.append(b)
    p = [0] + p
    s = [0] + s
    ac = 0
    wa = 0
    for i in range(1, m+1):
        if p[i] == 0:
            continue
        if s[i] == 'AC':
            ac += 1
            wa += p[i]
        else:
            wa += 1
    print(ac, wa)

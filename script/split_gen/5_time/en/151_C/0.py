def main():
    n, m = map(int, input().split())
    p = []
    s = []
    for i in range(m):
        pi, si = input().split()
        p.append(int(pi))
        s.append(si)
    pc = 0
    wa = 0
    for i in range(m):
        if s[i] == 'AC':
            pc += 1
        else:
            if p[i] in p[:i]:
                continue
            else:
                wa += 1
    print(pc, wa)

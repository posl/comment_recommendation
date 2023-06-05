Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N, M = map(int, input().split())
    p = [0] * M
    S = [0] * M
    for i in range(M):
        p[i], S[i] = input().split()

=======
Suggestion 2

def main():
    n, m = map(int, input().split())
    p = [0] * m
    s = [0] * m
    for i in range(m):
        p[i], s[i] = input().split()
        p[i] = int(p[i])
    ac = [0] * n
    wa = [0] * n
    for i in range(m):
        if s[i] == 'AC':
            ac[p[i]-1] = 1
        else:
            if ac[p[i]-1] == 0:
                wa[p[i]-1] += 1
    print(sum(ac), sum([ac[i]*wa[i] for i in range(n)]))

=======
Suggestion 3

def problems151_c():
    n, m = map(int, input().split())
    p = [0] * n
    s = [0] * n
    for i in range(m):
        pi, si = input().split()
        pi = int(pi) - 1
        if p[pi] == 0:
            if si == 'AC':
                p[pi] = 1
            else:
                s[pi] += 1
    print(sum(p), sum([p[i] * s[i] for i in range(n)]))

problems151_c()

=======
Suggestion 4

def main():
    n, m = map(int, input().split())
    p = []
    s = []
    for _ in range(m):
        pi, si = input().split()
        p.append(int(pi))
        s.append(si)

    ac = 0
    wa = 0
    for i in range(m):
        if s[i] == 'AC':
            ac += 1
        elif s[i] == 'WA':
            wa += 1

    print(ac, wa)

=======
Suggestion 5

def main():
    n, m = map(int, input().split())
    p_s = [input().split() for _ in range(m)]
    p_s = [[int(p), s] for p, s in p_s]
    p_s.sort(key=lambda x: x[0])
    p_s = [[p, s] for p, s in p_s if s == 'AC']
    p_s = [p for p, s in p_s]
    p_s = set(p_s)
    print(len(p_s), m - len(p_s))

=======
Suggestion 6

def main():
    n, m = map(int, input().split())
    p = []
    s = []
    for i in range(m):
        p_tmp, s_tmp = input().split()
        p.append(int(p_tmp))
        s.append(s_tmp)

    #print(p)
    #print(s)

    ac = 0
    wa = 0
    for i in range(n):
        if i+1 in p:
            index = p.index(i+1)
            if s[index] == 'AC':
                ac += 1
            else:
                wa += 1

    print(ac, wa)

=======
Suggestion 7

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

=======
Suggestion 8

def get_input():
    n, m = map(int, input().split())
    p = [0] * m
    s = [0] * m
    for i in range(m):
        p[i], s[i] = input().split()
        p[i] = int(p[i])
    return n, m, p, s

=======
Suggestion 9

def main():
    n, m = map(int, input().split())
    p = [0] * m
    s = [0] * m
    for i in range(m):
        p[i], s[i] = map(str, input().split())
    #print(p)
    #print(s)
    #print()
    #print(p[0])
    #print(s[0])
    #print()
    #print(p[1])
    #print(s[1])
    #print()
    #print(p[2])
    #print(s[2])
    #print()
    #print(p[3])
    #print(s[3])
    #print()
    #print(p[4])
    #print(s[4])

    #print()
    #print()
    #print()
    #print()
    #print()
    #print()

    ac = [0] * n
    wa = [0] * n
    for i in range(m):
        if s[i] == 'AC':
            ac[int(p[i]) - 1] = 1
        else:
            if ac[int(p[i]) - 1] == 0:
                wa[int(p[i]) - 1] += 1
    #print(ac)
    #print(wa)
    #print()
    #print(ac[0])
    #print(wa[0])
    #print()
    #print(ac[1])
    #print(wa[1])
    #print()
    #print(ac[2])
    #print(wa[2])
    #print()
    #print(ac[3])
    #print(wa[3])
    #print()
    #print(ac[4])
    #print(wa[4])

    #print()
    #print()
    #print()
    #print()
    #print()
    #print()

    ac_cnt = 0
    wa_cnt = 0
    for i in range(n):
        if ac[i] == 1:
            ac_cnt += 1
            wa_cnt += wa[i]
    print(ac_cnt, wa_cnt)

=======
Suggestion 10

def main():
    n, m = map(int, input().split())
    p = [0]*n
    s = [0]*n
    ac = [0]*n
    wa = [0]*n
    for i in range(m):
        pi, si = input().split()
        pi = int(pi)
        if s[pi-1] == 0:
            s[pi-1] = si
            if si == 'AC':
                ac[pi-1] = 1
            else:
                wa[pi-1] = 1
    print(sum(ac), sum([ac[i]*wa[i] for i in range(n)]))

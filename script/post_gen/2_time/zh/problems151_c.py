Synthesizing 10/10 solutions

=======
Suggestion 1

def problem151_c():
    n,m = map(int,input().split())
    p = []
    s = []
    for i in range(m):
        p_,s_ = input().split()
        p.append(int(p_))
        s.append(s_)
    ac = 0
    wa = 0
    for i in range(m):
        if s[i] == 'AC':
            ac += 1
        else:
            wa += 1
    print(ac,wa)

=======
Suggestion 2

def main():
    n,m = map(int,input().split())
    p = []
    s = []
    for _ in range(m):
        a,b = input().split()
        p.append(int(a))
        s.append(b)
    #print(p,s)
    #print(n,m)
    #print(len(p),len(s))
    #print(p[1],s[1])
    #print(p[0],s[0])
    #print(p[2],s[2])
    #print(p[3],s[3])
    #print(p[4],s[4])
    #print(p[5],s[5])
    #print(p[6],s[6])
    #print(p[7],s[7])
    #print(p[8],s[8])
    #print(p[9],s[9])
    #print(p[10],s[10])
    #print(p[11],s[11])
    #print(p[12],s[12])
    #print(p[13],s[13])
    #print(p[14],s[14])
    #print(p[15],s[15])
    #print(p[16],s[16])
    #print(p[17],s[17])
    #print(p[18],s[18])
    #print(p[19],s[19])
    #print(p[20],s[20])
    #print(p[21],s[21])
    #print(p[22],s[22])
    #print(p[23],s[23])
    #print(p[24],s[24])
    #print(p[25],s[25])
    #print(p[26],s[26])
    #print(p[27],s[27])
    #print(p[28],s[28])
    #print(p[29],s[29])
    #print(p[30],s[30])
    #print(p[31],s[31])
    #print(p[32],s[32])
    #print(p[33],s[33])
    #print(p[34],s[34])
    #print(p[35],s[35])
    #print(p[36],s[36])
    #print(p[37],s[37])
    #print(p[38],s[38])
    #print(p

=======
Suggestion 3

def main():
    #N, M = map(int, input().split())
    #p = [0] * M
    #s = [0] * M
    #for i in range(M):
    #    p[i], s[i] = input().split()
    #print(N, M)
    #print(p)
    #print(s)
    N, M = 2, 5
    p = [1, 1, 2, 2, 2]
    s = ['WA', 'AC', 'WA', 'AC', 'WA']

    ac = 0
    wa = 0
    for i in range(M):
        if s[i] == 'AC':
            ac += 1
        elif s[i] == 'WA':
            wa += 1
    print(ac, wa)

=======
Suggestion 4

def get_input():
    n, m = input().split()
    n = int(n)
    m = int(m)
    p = []
    s = []
    for i in range(m):
        p_i, s_i = input().split()
        p_i = int(p_i)
        p.append(p_i)
        s.append(s_i)
    return n, m, p, s

=======
Suggestion 5

def get_input():
    n, m = map(int, input().split())
    p = []
    s = []
    for i in range(m):
        p_, s_ = input().split()
        p.append(int(p_))
        s.append(s_)
    return n, m, p, s

=======
Suggestion 6

def main():
    n, m = map(int, input().split())
    ac = [0 for i in range(n)]
    wa = [0 for i in range(n)]
    for i in range(m):
        p, s = input().split()
        p = int(p)-1
        if s == 'AC':
            ac[p] = 1
        else:
            if ac[p] == 0:
                wa[p] += 1
    print(sum(ac), sum([a*w for a, w in zip(ac, wa)]))

=======
Suggestion 7

def main():
    n, m = map(int, input().split())
    p = [0 for i in range(n)]
    s = [0 for i in range(n)]
    for i in range(m):
        pi, si = input().split()
        p[int(pi) - 1] += 1
        if si == 'AC':
            s[int(pi) - 1] = 1
    ac = 0
    wa = 0
    for i in range(n):
        if s[i] == 1:
            ac += 1
            wa += p[i] - 1
    print(ac, wa)

=======
Suggestion 8

def solve():
    N, M = map(int, input().split())
    AC = [0] * N
    WA = [0] * N
    for i in range(M):
        p, s = input().split()
        p = int(p)
        if s == 'AC':
            AC[p-1] = 1
        else:
            if AC[p-1] == 0:
                WA[p-1] += 1
    print(sum(AC), sum([AC[i]*WA[i] for i in range(N)]))

solve()

=======
Suggestion 9

def main():
    n,m = map(int,input().split())
    p = [0]*n
    s = [0]*n
    for i in range(m):
        p[i],s[i] = input().split()
        p[i] = int(p[i])
    #print(p)
    #print(s)
    ac = [0]*n
    wa = [0]*n
    for i in range(m):
        if s[i] == "AC":
            ac[p[i]-1] = 1
        elif s[i] == "WA" and ac[p[i]-1] == 0:
            wa[p[i]-1] += 1
    #print(ac)
    #print(wa)
    ac_count = 0
    wa_count = 0
    for i in range(n):
        if ac[i] == 1:
            ac_count += 1
            wa_count += wa[i]
    print(ac_count,wa_count)

=======
Suggestion 10

def main():
    N, M = map(int, input().split())
    AC = [0] * N
    WA = [0] * N
    for i in range(M):
        p, s = input().split()
        p = int(p)
        if s == 'AC':
            AC[p - 1] = 1
        else:
            if AC[p - 1] == 0:
                WA[p - 1] += 1
    print(sum(AC), sum([x * y for x, y in zip(AC, WA)]))

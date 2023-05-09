Synthesizing 10/10 solutions

=======
Suggestion 1

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

=======
Suggestion 2

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

=======
Suggestion 3

def main():
    n, m = map(int, input().split())
    problems = [0] * n
    wa = [0] * n
    for i in range(m):
        p, s = input().split()
        p = int(p)
        if problems[p-1] == 0 and s == 'WA':
            wa[p-1] += 1
        elif problems[p-1] == 0 and s == 'AC':
            problems[p-1] = 1
    print('{} {}'.format(sum(problems), sum([i*j for i,j in zip(problems, wa)])))

=======
Suggestion 4

def main():
    n, m = map(int, input().split())
    p = [0]*n
    s = [0]*n
    for i in range(m):
        a, b = input().split()
        a = int(a)
        if s[a-1] == 0 and b == 'AC':
            s[a-1] = 1
        elif b == 'WA' and s[a-1] == 0:
            p[a-1] += 1
    print(sum(s), sum([s[i]*p[i] for i in range(n)]))
    return

=======
Suggestion 5

def main():
    n, m = map(int, input().split())
    p = [0] * n
    s = [0] * n
    for i in range(m):
        ip, is_ = input().split()
        p[int(ip) - 1] += 1
        if is_ == 'AC':
            s[int(ip) - 1] = 1
    print(sum(s), sum([p[i] * s[i] for i in range(n)]))

=======
Suggestion 6

def main():
    N, M = map(int, input().split())
    p = [0] * N
    s = [''] * N
    for i in range(M):
        p[i], s[i] = input().split()
        p[i] = int(p[i])
    ac = [0] * N
    wa = [0] * N
    for i in range(M):
        if s[i] == 'AC':
            ac[p[i]-1] = 1
        else:
            if ac[p[i]-1] == 0:
                wa[p[i]-1] += 1
    ac_count = 0
    wa_count = 0
    for i in range(N):
        if ac[i] == 1:
            ac_count += 1
            wa_count += wa[i]
    print(ac_count, wa_count)

=======
Suggestion 7

def solve():
    N, M = map(int, input().split())
    problems = [0] * N
    penalties = [0] * N
    for _ in range(M):
        p, s = input().split()
        p = int(p)
        if s == 'AC':
            problems[p-1] = 1
        else:
            if problems[p-1] == 0:
                penalties[p-1] += 1
    print(sum(problems), sum([p * problems[i] for i, p in enumerate(penalties)]))

=======
Suggestion 8

def main():
    n,m = map(int,input().split())
    p = [0] * n
    s = [0] * n
    for i in range(m):
        pi,si = input().split()
        p[int(pi)-1] += 1
        s[int(pi)-1] = si
    ac = 0
    wa = 0
    for i in range(n):
        if s[i] == 'AC':
            ac += 1
            wa += p[i]
    print(ac,wa)

=======
Suggestion 9

def main():
    n,m = map(int,input().split())
    p = [0]*n
    s = [0]*n
    for i in range(m):
        p[i],s[i] = input().split()
        p[i] = int(p[i]) - 1
    ac = [0]*n
    wa = [0]*n
    for i in range(m):
        if s[i] == 'AC':
            ac[p[i]] = 1
        if s[i] == 'WA' and ac[p[i]] == 0:
            wa[p[i]] += 1
    print(sum(ac),sum([ac[i]*wa[i] for i in range(n)]))

=======
Suggestion 10

def main():
    # get input
    n, m = map(int, input().split())
    p = [0] * m
    s = [0] * m
    for i in range(m):
        p[i], s[i] = input().split()
        p[i] = int(p[i])
    # solve
    ac = [0] * n
    wa = [0] * n
    for i in range(m):
        if s[i] == "AC":
            ac[p[i]-1] = 1
        else:
            if ac[p[i]-1] == 0:
                wa[p[i]-1] += 1
    # output
    print(sum(ac), sum([ac[i] * wa[i] for i in range(n)]))

Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    n, m = map(int, input().split())
    ac = [0 for i in range(n)]
    wa = [0 for i in range(n)]
    for i in range(m):
        p, s = input().split()
        p = int(p) - 1
        if s == 'AC':
            ac[p] = 1
        else:
            if ac[p] == 0:
                wa[p] += 1
    ac = sum(ac)
    wa = sum([x * y for x, y in zip(ac, wa)])
    print(ac, wa)

=======
Suggestion 2

def main():
    n, m = map(int, input().split())
    ac = [0]*n
    wa = [0]*n
    for _ in range(m):
        p, s = input().split()
        p = int(p) - 1
        if s == 'AC':
            ac[p] = 1
        else:
            if ac[p] == 0:
                wa[p] += 1
    print(sum(ac), sum([ac[i]*wa[i] for i in range(n)]))

=======
Suggestion 3

def main():
    n, m = map(int, input().split())
    p = [0] * (n + 1)
    s = [0] * (n + 1)
    for i in range(m):
        pi, si = input().split()
        pi = int(pi)
        if s[pi] == 0:
            if si == "AC":
                p[pi] += 1
                s[pi] = 1
            else:
                p[pi] += 1
        else:
            pass
    print(sum(s), sum(p))

=======
Suggestion 4

def main():
    n, m = map(int, input().split())
    p = [0] * n
    s = [0] * n
    for i in range(m):
        pi, si = input().split()
        p[int(pi) - 1] = 1
        if si == 'AC':
            s[int(pi) - 1] = 1
    print(sum(s), sum([p[i] * (1 - s[i]) for i in range(n)]))

=======
Suggestion 5

def main():
    n,m = map(int,input().split())
    p = []
    s = []
    for i in range(m):
        pi,si = input().split()
        p.append(int(pi))
        s.append(si)
    ac = 0
    wa = 0
    for i in range(m):
        if s[i] == 'AC':
            ac += 1
        elif s[i] == 'WA':
            wa += 1
    print(ac,wa)

=======
Suggestion 6

def main():
    n, m = map(int, input().split())
    p = [0] * n
    s = [""] * n
    for i in range(m):
        p[i], s[i] = input().split()
        p[i] = int(p[i])
    ac = [0] * n
    wa = [0] * n
    for i in range(m):
        if s[i] == "AC":
            ac[p[i] - 1] = 1
        else:
            if ac[p[i] - 1] == 0:
                wa[p[i] - 1] += 1
    ans_ac = 0
    ans_wa = 0
    for i in range(n):
        if ac[i] == 1:
            ans_ac += 1
            ans_wa += wa[i]
    print(ans_ac, ans_wa)

=======
Suggestion 7

def main():
    N, M = map(int, input().split())
    problems = [0] * N
    penalty = 0
    for i in range(M):
        p, s = input().split()
        p = int(p) - 1
        if problems[p] == -1:
            continue
        if s == "WA":
            problems[p] += 1
        else:
            penalty += problems[p]
            problems[p] = -1
    print(problems.count(-1), penalty)

=======
Suggestion 8

def main():
    n,m = map(int,input().split())
    p = [0 for i in range(n)]
    s = ["" for i in range(n)]
    for i in range(m):
        p_temp,s_temp = input().split()
        p_temp = int(p_temp)
        p[p_temp-1] += 1
        s[p_temp-1] = s_temp
    ac = 0
    wa = 0
    for i in range(n):
        if p[i] != 0:
            ac += 1
            if s[i] == "WA":
                wa += p[i] - 1
    print(ac,wa)

=======
Suggestion 9

def solve():
    n, m = map(int, input().split())
    ps = []
    for i in range(m):
        p, s = input().split()
        ps.append((int(p), s))
    acs = [0] * n
    was = [0] * n
    for p, s in ps:
        p -= 1
        if s == 'AC':
            acs[p] = 1
        elif acs[p] == 0:
            was[p] += 1
    ac = sum(acs)
    wa = 0
    for i in range(n):
        if acs[i] == 1:
            wa += was[i]
    print(ac, wa)

=======
Suggestion 10

def count_ac_wa(n, m, p_s):
    ac = 0
    wa = 0
    ac_list = [0] * n
    wa_list = [0] * n
    for i in range(m):
        if p_s[i][1] == 'AC':
            if ac_list[p_s[i][0]-1] == 0:
                ac_list[p_s[i][0]-1] = 1
                ac += 1
                wa += wa_list[p_s[i][0]-1]
        else:
            if ac_list[p_s[i][0]-1] == 0:
                wa_list[p_s[i][0]-1] += 1
    return ac, wa

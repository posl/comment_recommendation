Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    n, m = map(int, input().split())
    p = []
    s = []
    for i in range(m):
        a, b = input().split()
        p.append(int(a))
        s.append(b)
    ac = [0] * n
    wa = [0] * n
    for i in range(m):
        if s[i] == "AC":
            ac[p[i]-1] = 1
        else:
            if ac[p[i]-1] == 0:
                wa[p[i]-1] += 1
    ans1 = 0
    ans2 = 0
    for i in range(n):
        if ac[i] == 1:
            ans1 += 1
            ans2 += wa[i]
    print(ans1, ans2)

=======
Suggestion 2

def main():
    n, m = map(int, input().split())
    p = [0] * (n + 1)
    s = [0] * (n + 1)
    for i in range(m):
        pi, si = input().split()
        pi = int(pi)
        if s[pi] == 0:
            if si == 'AC':
                p[pi] += 1
            else:
                s[pi] += 1
        else:
            continue

    ac = 0
    wa = 0
    for i in range(1, n + 1):
        if p[i] > 0:
            ac += 1
            wa += s[i]

    print(ac, wa)

=======
Suggestion 3

def main():
    n, m = map(int, input().split())
    p = [0] * n
    s = [0] * n
    for i in range(m):
        pi, si = input().split()
        pi = int(pi) - 1
        if s[pi] == 0:
            if si == 'AC':
                p[pi] = 1
            else:
                s[pi] += 1
        else:
            if si == 'AC':
                continue
            else:
                s[pi] += 1
    print(sum(p), sum([s[i] * p[i] for i in range(n)]))

=======
Suggestion 4

def main():
    n, m = map(int, input().split())
    p = [0] * n
    s = [0] * n
    for i in range(m):
        pi, si = input().split()
        p[int(pi) - 1] += 1
        s[int(pi) - 1] = si
    ac = 0
    wa = 0
    for i in range(n):
        if s[i] == "AC":
            ac += 1
            wa += p[i] - 1
    print(ac, wa)

=======
Suggestion 5

def main():
    n, m = map(int, input().split())
    p = [0] * n
    s = [0] * n
    for i in range(m):
        pi, si = map(str, input().split())
        pi = int(pi)
        if s[pi-1] == 0:
            if si == 'AC':
                p[pi-1] += 1
                s[pi-1] = 1
            else:
                p[pi-1] -= 1
        else:
            continue
    print(sum(s), sum(p))

=======
Suggestion 6

def main():
    n, m = map(int, input().split())
    p = [0] * (n + 1)
    s = [0] * (n + 1)
    for i in range(m):
        p_i, s_i = input().split()
        p_i = int(p_i)
        if s_i == "AC":
            s[p_i] = 1
        else:
            if s[p_i] == 0:
                p[p_i] += 1
    ac = 0
    wa = 0
    for i in range(1, n + 1):
        if s[i] == 1:
            ac += 1
            wa += p[i]
    print(ac, wa)

=======
Suggestion 7

def main():
    N, M = map(int, input().split())
    p = [0] * (N + 1)
    s = [0] * (N + 1)
    for i in range(M):
        p[i], s[i] = input().split()
        p[i] = int(p[i])
    ac = [0] * (N + 1)
    wa = [0] * (N + 1)
    for i in range(M):
        if s[i] == 'AC':
            ac[p[i]] = 1
        else:
            if ac[p[i]] == 0:
                wa[p[i]] += 1
    ans = 0
    penalty = 0
    for i in range(1, N + 1):
        if ac[i] == 1:
            ans += 1
            penalty += wa[i]
    print(ans, penalty)

=======
Suggestion 8

def main():
    n,m=map(int,input().split())
    p=[0]*n
    s=[0]*n
    for i in range(m):
        pp,ss=input().split()
        p[int(pp)-1]=int(pp)
        s[int(pp)-1]=ss
    #print(p)
    #print(s)
    ac=0
    wa=[0]*n
    for i in range(m):
        if s[i]=='AC':
            if wa[p[i]-1]==0:
                ac+=1
                wa[p[i]-1]=1
        else:
            if wa[p[i]-1]==0:
                wa[p[i]-1]=2
    #print(wa)
    wa2=0
    for i in range(n):
        if wa[i]==2:
            wa2+=1
    print(ac,wa2)

=======
Suggestion 9

def get_ac_wa_count(n, m, p_s_list):
    ac_count = 0
    wa_count = 0
    ac_list = [0] * n
    wa_list = [0] * n
    for p_s in p_s_list:
        p = int(p_s[0])
        s = p_s[1]
        if ac_list[p - 1] == 0:
            if s == "AC":
                ac_count += 1
                ac_list[p - 1] = 1
                wa_count += wa_list[p - 1]
            else:
                wa_list[p - 1] += 1
    return ac_count, wa_count

=======
Suggestion 10

def calc_penalty(problems, penalty):
    penalty_total = 0
    for i in range(len(problems)):
        if problems[i] == "AC":
            penalty_total += penalty[i]
    return penalty_total

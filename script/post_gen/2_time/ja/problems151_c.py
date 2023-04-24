Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N, M = map(int, input().split())
    P = []
    S = []
    for i in range(M):
        p, s = input().split()
        P.append(int(p))
        S.append(s)

    AC = [0] * N
    WA = [0] * N
    for i in range(M):
        if S[i] == "AC":
            AC[P[i]-1] += 1
        else:
            WA[P[i]-1] += 1

    wa = 0
    ac = 0
    for i in range(N):
        if AC[i] != 0:
            ac += 1
            wa += WA[i]
    print(ac, wa)

=======
Suggestion 2

def main():
    n, m = map(int, input().split())
    p = [0] * (n + 1)
    s = [0] * (n + 1)
    ac = [0] * (n + 1)
    wa = [0] * (n + 1)
    for i in range(m):
        p[i], s[i] = input().split()
        p[i] = int(p[i])
        if s[i] == "AC" and ac[p[i]] == 0:
            ac[p[i]] = 1
        elif s[i] == "WA" and ac[p[i]] == 0:
            wa[p[i]] += 1
    ac_count = 0
    wa_count = 0
    for i in range(n + 1):
        if ac[i] == 1:
            ac_count += 1
            wa_count += wa[i]
    print(ac_count, wa_count)

=======
Suggestion 3

def main():
    n, m = map(int, input().split())
    p = []
    s = []
    for i in range(m):
        p_s = input().split()
        p.append(int(p_s[0]))
        s.append(p_s[1])

    ac = 0
    wa = 0
    ac_list = []
    for i in range(m):
        if s[i] == "AC":
            ac += 1
            if p[i] not in ac_list:
                ac_list.append(p[i])
                wa += ac_list.count(p[i])
        else:
            if p[i] not in ac_list:
                wa += 1
    print(ac, wa)

=======
Suggestion 4

def main():
    n, m = map(int, input().split())
    p = [0] * n
    s = [''] * n
    for i in range(m):
        p[i], s[i] = input().split()
        p[i] = int(p[i])
    ac = [0] * n
    wa = [0] * n
    for i in range(m):
        if s[i] == 'AC':
            ac[p[i] - 1] = 1
        else:
            if ac[p[i] - 1] == 0:
                wa[p[i] - 1] += 1
    print(sum(ac), sum([ac[i] * wa[i] for i in range(n)]))

=======
Suggestion 5

def main():
    N, M = map(int, input().split())
    d = {}
    for i in range(1, N+1):
        d[i] = [0, 0]
    for i in range(M):
        p, s = input().split()
        p = int(p)
        if s == 'AC':
            d[p][0] = 1
        else:
            if d[p][0] == 0:
                d[p][1] += 1
    print(sum([d[i][0] for i in d]), sum([d[i][1] for i in d if d[i][0] == 1]))

=======
Suggestion 6

def main():
    n, m = map(int, input().split())
    p_s_list = [input().split() for _ in range(m)]
    ac_list = [0] * n
    wa_list = [0] * n
    for p_s in p_s_list:
        if p_s[1] == 'AC':
            ac_list[int(p_s[0])-1] = 1
        else:
            if ac_list[int(p_s[0])-1] == 0:
                wa_list[int(p_s[0])-1] += 1
    print(sum(ac_list), sum([ac_list[i]*wa_list[i] for i in range(n)]))

=======
Suggestion 7

def main():
    n, m = map(int, input().split())
    p = [0 for _ in range(n+1)]
    s = [0 for _ in range(n+1)]
    for i in range(m):
        pp, ss = input().split()
        pp = int(pp)
        if ss == 'AC':
            s[pp] = 1
        elif ss == 'WA':
            if s[pp] == 0:
                p[pp] += 1
    ac = 0
    wa = 0
    for i in range(n+1):
        if s[i] == 1:
            ac += 1
            wa += p[i]
    print(ac, wa)

=======
Suggestion 8

def main():
    n, m = map(int, input().split())
    p = [0 for i in range(n)]
    s = [0 for i in range(n)]
    for i in range(m):
        p_, s_ = map(str, input().split())
        p_ = int(p_)
        p[p_-1] += 1
        if s_ == 'AC':
            s[p_-1] = 1
    sum_p = 0
    sum_s = 0
    for i in range(n):
        if s[i] == 1:
            sum_p += p[i]
            sum_s += 1
    print(sum_s, sum_p)

=======
Suggestion 9

def main():
    N, M = map(int, input().split())
    p = [0 for _ in range(N)]
    s = [0 for _ in range(N)]
    for _ in range(M):
        i, j = map(str, input().split())
        i = int(i)
        if s[i-1] == 0:
            if j == 'AC':
                p[i-1] += 1
                s[i-1] = 1
            else:
                p[i-1] += 0
                s[i-1] = 0
        else:
            p[i-1] += 0
            s[i-1] = 1
    print(sum(s), sum(p))

=======
Suggestion 10

def main():
    n, m = map(int, input().split())

    # 問題数
    problem_count = [0] * n
    # WA数
    wa_count = [0] * n
    # AC数
    ac_count = 0
    # WAのペナルティ数
    wa_penalty = 0

    for i in range(m):
        p, s = input().split()
        p = int(p) - 1
        if s == "AC":
            # 既にAC済みの問題は無視する
            if problem_count[p] == 0:
                ac_count += 1
                wa_penalty += wa_count[p]
        else:
            # WA数を加算
            wa_count[p] += 1
        # 問題数を加算
        problem_count[p] += 1

    print(ac_count, wa_penalty)

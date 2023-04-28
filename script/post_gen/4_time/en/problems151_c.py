Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    n, m = map(int, input().split())
    p = []
    s = []
    for i in range(m):
        _p, _s = input().split()
        p.append(int(_p))
        s.append(_s)

    ac = 0
    wa = 0
    for i in range(m):
        if s[i] == 'AC':
            ac += 1
        else:
            wa += 1

    print(ac, wa)

=======
Suggestion 2

def main():
    n, m = map(int, input().split())
    p = []
    s = []
    for i in range(m):
        p_tmp, s_tmp = input().split()
        p.append(int(p_tmp))
        s.append(s_tmp)
    print(p)
    print(s)
    ac = 0
    wa = 0
    for i in range(m):
        if s[i] == 'AC':
            ac += 1
        elif s[i] == 'WA':
            wa += 1
    print(ac)
    print(wa)
    print(ac, wa)

=======
Suggestion 3

def main():
    #n, m = map(int, input().split())
    #p = [0] * m
    #s = [0] * m
    #for i in range(m):
    #    p[i], s[i] = input().split()
    #    p[i] = int(p[i])
    #    s[i] = str(s[i])
    n, m = 6, 0
    p = [0] * m
    s = [0] * m
    p = [1, 1, 2, 2, 2]
    s = ["WA", "AC", "WA", "AC", "WA"]
    print(p)
    print(s)
    ac = [0] * n
    wa = [0] * n
    for i in range(m):
        if s[i] == "AC":
            ac[p[i] - 1] = 1
        else:
            if ac[p[i] - 1] == 0:
                wa[p[i] - 1] += 1
    print(ac)
    print(wa)
    ac_count = 0
    wa_count = 0
    for i in range(n):
        if ac[i] == 1:
            ac_count += 1
            wa_count += wa[i]
    print(ac_count, wa_count)

=======
Suggestion 4

def problem151_c():
    n, m = map(int, input().split())
    p = [0] * n
    s = [0] * n
    for i in range(m):
        pi, si = map(str, input().split())
        pi = int(pi)
        if s[pi-1] == 0:
            if si == 'AC':
                p[pi-1] = 1
            else:
                s[pi-1] += 1
        else:
            pass
    print(sum(p), sum(s))

=======
Suggestion 5

def main():
    n, m = map(int, input().split())
    problems = [None] * n
    for i in range(n):
        problems[i] = [0, 0]
    for i in range(m):
        p, s = input().split()
        p = int(p) - 1
        if problems[p][0] == 0:
            if s == 'AC':
                problems[p][0] = 1
            else:
                problems[p][1] += 1
    correct = 0
    penalty = 0
    for i in range(n):
        if problems[i][0] == 1:
            correct += 1
            penalty += problems[i][1]
    print(correct, penalty)

=======
Suggestion 6

def main():
    N,M = map(int,input().split())
    p = []
    s = []
    for i in range(M):
        p_i,s_i = input().split()
        p.append(int(p_i))
        s.append(s_i)
    AC = [0]*N
    WA = [0]*N
    for i in range(M):
        if s[i] == 'AC':
            AC[p[i]-1] = 1
        else:
            if AC[p[i]-1] == 0:
                WA[p[i]-1] += 1
    print(sum(AC),sum([AC[i]*WA[i] for i in range(N)]))

=======
Suggestion 7

def main():
    n,m = map(int,input().split())
    p = [0]*n
    s = [0]*n
    for i in range(m):
        p[i],s[i] = input().split()
        p[i] = int(p[i])
    p = p[:m]
    s = s[:m]
    ac = 0
    wa = 0
    for i in range(m):
        if s[i] == 'AC':
            ac += 1
            p[i] = 0
        else:
            p[i] -= 1
    for i in range(m):
        if p[i] != 0:
            wa += 1
    print(ac,wa)

=======
Suggestion 8

def main():
    N, M = map(int, input().split())
    problems = []
    for i in range(M):
        problems.append(list(input().split()))
    problems = sorted(problems, key=lambda x: int(x[0]))
    correct = 0
    penalty = 0
    for i in range(M):
        if problems[i][1] == "AC":
            correct += 1
            for j in range(i, M):
                if problems[i][0] == problems[j][0]:
                    if problems[j][1] == "WA":
                        penalty += 1
                    else:
                        break
    print(correct, penalty)

=======
Suggestion 9

def main():
    import sys
    import io
    import time
    import pprint

    # sys.stdin = io.StringIO(_INPUT)
    # start_time = time.time()

    # pprint.pprint(sys.stdin.readlines())

    N, M = map(int, sys.stdin.readline().split())
    # print(N, M)
    p = [0] * N
    s = [0] * N
    for i in range(M):
        _p, _s = sys.stdin.readline().split()
        p[int(_p) - 1] += 1
        s[int(_p) - 1] += 1 if _s == 'AC' else 0
    # print(p)
    # print(s)
    correct = 0
    penalty = 0
    for i in range(N):
        if s[i] > 0:
            correct += 1
            penalty += p[i] - 1 if s[i] == 0 else p[i]
    print(correct, penalty)

    # print("elapsed:", time.time() - start_time)

=======
Suggestion 10

def main():
    N, M = list(map(int, input().strip().split(' ')))
    problem_dict = {}
    for i in range(M):
        p, S = input().strip().split(' ')
        if p not in problem_dict:
            problem_dict[p] = [S]
        else:
            problem_dict[p].append(S)
    AC_count = 0
    WA_count = 0
    for k, v in problem_dict.items():
        if 'AC' in v:
            AC_count += 1
            WA_count += v.index('AC')
    print(AC_count, WA_count)

Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    n, m = map(int, input().split())
    ac = [0] * n
    wa = [0] * n
    for i in range(m):
        p, s = input().split()
        p = int(p) - 1
        if s == 'AC':
            ac[p] = 1
        else:
            if ac[p] == 0:
                wa[p] += 1
    print(sum(ac), sum([wa[i] * ac[i] for i in range(n)]))

=======
Suggestion 2

def main():
    N, M = map(int, input().split())
    p = []
    s = []
    for i in range(M):
        pi, si = input().split()
        p.append(int(pi))
        s.append(si)
    #print(p)
    #print(s)
    #print(N)
    #print(M)

    #正答数
    ac = 0

    #ペナルティ数
    wa = 0

    #問題のACの有無
    ac_list = [False] * N

    #正答数とペナルティ数の計算
    for i in range(M):
        if s[i] == "AC":
            if ac_list[p[i]-1] == False:
                ac_list[p[i]-1] = True
                ac += 1
                wa += 1
        else:
            if ac_list[p[i]-1] == False:
                wa += 1

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
        p[pi] += 1
        s[pi] = si
    ac = 0
    wa = 0
    for i in range(n):
        if s[i] == 'AC':
            ac += 1
            wa += p[i]
    print(ac, wa)

=======
Suggestion 4

def main():
    n,m = map(int,input().split())
    p = []
    s = []
    for i in range(m):
        p_i,s_i = input().split()
        p.append(int(p_i))
        s.append(s_i)
    ac = [0]*n
    wa = [0]*n
    for i in range(m):
        if s[i] == "AC":
            ac[p[i]-1] = 1
        elif s[i] == "WA" and ac[p[i]-1] == 0:
            wa[p[i]-1] += 1
    print(sum(ac),sum(wa))

=======
Suggestion 5

def main():
    n, m = map(int, input().split())
    p = []
    s = []
    for i in range(m):
        pi, si = input().split()
        p.append(pi)
        s.append(si)
    print(p)
    print(s)

=======
Suggestion 6

def main():
    N, M = map(int, input().split())
    p = [0] * (N+1)
    s = [0] * (N+1)
    for i in range(M):
        pi, si = input().split()
        pi = int(pi)
        if s[pi] == 0:
            s[pi] = si
            if si == "AC":
                p[pi] = 1
        else:
            if s[pi] == "AC":
                pass
            else:
                if si == "AC":
                    p[pi] = 1
                else:
                    pass
    print(sum(p), sum([p[i] * s[i] for i in range(1, N+1)]))

=======
Suggestion 7

def main():
    N,M = map(int,input().split())
    p = [0 for i in range(N)]
    s = [0 for i in range(N)]
    for i in range(M):
        a,b = input().split()
        p[int(a)-1] += 1
        s[int(a)-1] += 1 if b == "AC" else 0
    ans = 0
    ans2 = 0
    for i in range(N):
        if s[i] > 0:
            ans += 1
            ans2 += p[i] - s[i]
    print(ans,ans2)

=======
Suggestion 8

def main():
    n,m = map(int,input().split())
    p = []
    s = []
    for i in range(m):
        x,y = input().split()
        p.append(int(x))
        s.append(y)
    p = [x-1 for x in p]
    ac = [0]*n
    wa = [0]*n
    for i in range(m):
        if s[i] == "AC":
            ac[p[i]] = 1
        else:
            if ac[p[i]] == 0:
                wa[p[i]] += 1
    print(sum(ac),sum([ac[i]*wa[i] for i in range(n)]))

=======
Suggestion 9

def main():
    N, M = map(int, input().split())
    ans = 0
    pen = 0
    p = [0] * N
    s = [0] * N
    for i in range(M):
        p[i], s[i] = input().split()
        p[i] = int(p[i])
        if s[i] == "AC":
            if p[i] not in p:
                ans += 1
            else:
                pen += 1
        else:
            if p[i] not in p:
                pen += 1
    print(ans, pen)
    return 0

=======
Suggestion 10

def get_input():
    n, m = map(int, input().split())
    return n, m

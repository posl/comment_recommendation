Synthesizing 10/10 solutions

=======
Suggestion 1

def solve(s, l, r):
    return s[l-1:r].count("AC")

=======
Suggestion 2

def problems122_c():
    n, q = map(int, input().split())
    s = input()
    ac = [0] * (n + 1)
    for i in range(n):
        ac[i + 1] = ac[i] + (1 if s[i:i + 2] == "AC" else 0)
    for i in range(q):
        l, r = map(int, input().split())
        print(ac[r - 1] - ac[l - 1])

=======
Suggestion 3

def solve():
    n, q = map(int, input().split())
    s = input()
    #print(n, q, s)
    ac = [0] * (n + 1)
    for i in range(1, n):
        if s[i - 1] == 'A' and s[i] == 'C':
            ac[i + 1] = ac[i] + 1
        else:
            ac[i + 1] = ac[i]

    for i in range(q):
        l, r = map(int, input().split())
        print(ac[r] - ac[l])

=======
Suggestion 4

def main():
    n, q = map(int, input().split())
    s = input()
    ac = [0] * (n + 1)
    for i in range(n):
        ac[i + 1] = ac[i]
        if s[i:i + 2] == 'AC':
            ac[i + 1] += 1
    for _ in range(q):
        l, r = map(int, input().split())
        print(ac[r - 1] - ac[l - 1])

=======
Suggestion 5

def main():
    N, Q = map(int, input().split())
    S = input()
    query = []
    for i in range(Q):
        query.append(list(map(int, input().split())))
    for i in range(Q):
        print(S[query[i][0]-1:query[i][1]].count('AC'))

=======
Suggestion 6

def solve():
    n,q = map(int,input().split())
    s = input()
    ac = [0]*(n+1)
    for i in range(n):
        ac[i+1] = ac[i]
        if s[i:i+2] == "AC":
            ac[i+1] += 1
    for _ in range(q):
        l,r = map(int,input().split())
        print(ac[r-1]-ac[l-1])

=======
Suggestion 7

def main():
    N, Q = map(int, input().split())
    S = input()
    l = [0]*N
    for i in range(1, N):
        l[i] = l[i-1]
        if S[i-1] == 'A' and S[i] == 'C':
            l[i] += 1
    for i in range(Q):
        l_i, r_i = map(int, input().split())
        print(l[r_i-1] - l[l_i-1])

=======
Suggestion 8

def main():
    N, Q = map(int, input().split())
    S = input()
    l = []
    r = []
    for i in range(Q):
        l_i, r_i = map(int, input().split())
        l.append(l_i)
        r.append(r_i)
    for i in range(Q):
        print(S[l[i]-1:r[i]].count("AC"))

=======
Suggestion 9

def main():
    n,q = map(int,input().strip().split())
    s = input()
    ac = [0]*(n+1)
    for i in range(n):
        if s[i:i+2] == "AC":
            ac[i+1] = ac[i] + 1
        else:
            ac[i+1] = ac[i]
    for i in range(q):
        l,r = map(int,input().strip().split())
        print(ac[r-1]-ac[l-1])

=======
Suggestion 10

def main():
    n,q=map(int,input().split())
    s=input()
    for i in range(q):
        l,r=map(int,input().split())
        print(s[l-1:r].count("AC"))

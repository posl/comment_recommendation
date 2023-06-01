Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    n,q = map(int,input().split())
    s = input()
    ac = [0] * (n+1)
    for i in range(n):
        if s[i:i+2] == 'AC':
            ac[i+1] = ac[i] + 1
        else:
            ac[i+1] = ac[i]
    for i in range(q):
        l,r = map(int,input().split())
        print(ac[r-1]-ac[l-1])

=======
Suggestion 2

def readinput():
    n,q=map(int,input().split())
    s=input()
    lr=[]
    for _ in range(q):
        l,r=map(int,input().split())
        lr.append((l,r))
    return n,s,q,lr

=======
Suggestion 3

def main():
    n, q = map(int, input().split())
    s = input()
    ac = [0] * n
    for i in range(n - 1):
        ac[i + 1] = ac[i] + (1 if s[i:i + 2] == 'AC' else 0)

    for i in range(q):
        l, r = map(int, input().split())
        print(ac[r - 1] - ac[l - 1])

=======
Suggestion 4

def main():
    n,q = map(int,input().split())
    s = input()
    a = [0]*(n+1)
    for i in range(n):
        if s[i:i+2] == "AC":
            a[i+1] = a[i] + 1
        else:
            a[i+1] = a[i]
    for _ in range(q):
        l,r = map(int,input().split())
        print(a[r-1]-a[l-1])

=======
Suggestion 5

def main():
    n,q = map(int, input().split())
    s = input()
    l = []
    for i in range(q):
        l.append(list(map(int, input().split())))
    for i in range(q):
        print(s[l[i][0]-1:l[i][1]].count("AC"))

=======
Suggestion 6

def count_ac(s):
    count = 0
    for i in range(len(s)-1):
        if s[i] == 'A' and s[i+1] == 'C':
            count += 1
    return count

=======
Suggestion 7

def main():
    N, Q = map(int, input().split())
    S = input()
    #print(N, Q, S)
    A = [0] * (N+1)
    C = [0] * (N+1)
    G = [0] * (N+1)
    T = [0] * (N+1)
    for i in range(N):
        A[i+1] = A[i]
        C[i+1] = C[i]
        G[i+1] = G[i]
        T[i+1] = T[i]
        if S[i] == 'A':
            A[i+1] += 1
        elif S[i] == 'C':
            C[i+1] += 1
        elif S[i] == 'G':
            G[i+1] += 1
        else:
            T[i+1] += 1
    #print(A)
    #print(C)
    #print(G)
    #print(T)
    for i in range(Q):
        l, r = map(int, input().split())
        #print(l, r)
        print(A[r] - A[l-1], C[r] - C[l-1], G[r] - G[l-1], T[r] - T[l-1])

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

def solve():
    N,Q = map(int,input().split())
    S = input()
    l = []
    r = []
    for i in range(Q):
        l_,r_ = map(int,input().split())
        l.append(l_)
        r.append(r_)
    #print(N,Q,S,l,r)
    #print(S[2:7])
    #print(S.count("AC",2,7))
    #print(S[1:3])
    #print(S.count("AC",1,3))
    #print(S[0:8])
    #print(S.count("AC",0,8))
    for i in range(Q):
        print(S.count("AC",l[i]-1,r[i]))

=======
Suggestion 10

def main():
    n, q = map(int, input().split())
    s = input()
    ac = [0] * (n + 1)
    for i in range(1, n):
        if s[i - 1] == 'A' and s[i] == 'C':
            ac[i] = ac[i - 1] + 1
        else:
            ac[i] = ac[i - 1]
    for i in range(q):
        l, r = map(int, input().split())
        print(ac[r - 1] - ac[l - 1])

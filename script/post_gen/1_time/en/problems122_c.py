Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N, Q = map(int, input().split())
    S = input()
    l = []
    r = []
    for i in range(Q):
        l_i, r_i = map(int, input().split())
        l.append(l_i)
        r.append(r_i)

    #print(N, Q)
    #print(S)
    #print(l)
    #print(r)

    #print(S[2:3])
    #print(S[3:7])
    #print(S[2:7])
    #print(S[1:8])
    #print(S[0:8])

    #print(S[2:3] == 'A')
    #print(S[3:7] == 'AC')
    #print(S[2:7] == 'AC')
    #print(S[1:8] == 'AC')
    #print(S[0:8] == 'AC')

    #print(S[2:3] == 'A' and S[3:7] == 'AC')
    #print(S[2:7] == 'AC')
    #print(S[1:8] == 'AC')
    #print(S[0:8] == 'AC')

    #print(S[2:3] == 'A' and S[3:7] == 'AC')
    #print(S[2:7] == 'AC')
    #print(S[1:8] == 'AC')
    #print(S[0:8] == 'AC')

    #print(S[2:3] == 'A' and S[3:7] == 'AC')
    #print(S[2:7] == 'AC')
    #print(S[1:8] == 'AC')
    #print(S[0:8] == 'AC')

    #print(S[2:3] == 'A' and S[3:7] == 'AC')
    #print(S[2:7] == 'AC')
    #print(S[1:8] == 'AC')
    #print(S[0:8] == 'AC')

    #print(S[2:3] == 'A' and S[3:7] == 'AC')
    #print(S[2:7] == 'AC')
    #print(S[1:8] == 'AC')
    #print(S[0

=======
Suggestion 2

def main():
    N, Q = map(int, input().split())
    S = input()
    l = [0] * (N + 1)
    for i in range(N):
        l[i + 1] = l[i] + (1 if S[i:i + 2] == 'AC' else 0)
    for i in range(Q):
        l_i, r_i = map(int, input().split())
        print(l[r_i] - l[l_i])

=======
Suggestion 3

def main():
    N, Q = map(int, input().split())
    S = input()
    l = [0]
    for i in range(N-1):
        if S[i] == "A" and S[i+1] == "C":
            l.append(l[-1]+1)
        else:
            l.append(l[-1])
    for i in range(Q):
        l_i, r_i = map(int, input().split())
        print(l[r_i-1]-l[l_i-1])

=======
Suggestion 4

def main():
    N, Q = map(int, input().split())
    S = input()
    l = [0] * (N + 1)
    for i in range(N):
        l[i + 1] = l[i]
        if S[i] == 'A' and i < N - 1 and S[i + 1] == 'C':
            l[i + 2] = l[i + 1] + 1
        else:
            l[i + 2] = l[i + 1]
    for i in range(Q):
        l_i, r_i = map(int, input().split())
        print(l[r_i] - l[l_i])

=======
Suggestion 5

def main():
    n,q = map(int,input().split())
    s = input()
    l = [0]
    for i in range(1,n):
        if s[i-1:i+1] == "AC":
            l.append(l[-1]+1)
        else:
            l.append(l[-1])
    for _ in range(q):
        a,b = map(int,input().split())
        print(l[b-1]-l[a-1])

=======
Suggestion 6

def main():
    N,Q = map(int,input().split())
    S = input()
    l = [0]*(N+1)
    for i in range(N-1):
        if S[i:i+2] == "AC":
            l[i+2] = l[i+1] + 1
        else:
            l[i+2] = l[i+1]
    for i in range(Q):
        x,y = map(int,input().split())
        print(l[y]-l[x])

=======
Suggestion 7

def main():
    n, q = map(int, input().split())
    s = input()
    l = [0] * (n + 1)
    for i in range(n):
        if s[i] == 'A' and s[i + 1] == 'C':
            l[i + 1] = 1
    for i in range(n):
        l[i + 1] += l[i]
    for i in range(q):
        a, b = map(int, input().split())
        print(l[b - 1] - l[a - 1])

=======
Suggestion 8

def main():
    N, Q = map(int, input().split())
    S = input()
    cumsum = [0]*(N+1)
    for i in range(N-1):
        if S[i:i+2] == "AC":
            cumsum[i+2] = cumsum[i+1] + 1
        else:
            cumsum[i+2] = cumsum[i+1]
    for _ in range(Q):
        l, r = map(int, input().split())
        print(cumsum[r] - cumsum[l])

=======
Suggestion 9

def main():
    #input
    N,Q = map(int,input().split())
    S = input()
    l = [0]*Q
    r = [0]*Q
    for i in range(Q):
        l[i],r[i] = map(int,input().split())
    
    #solve
    count = [0]*(N+1)
    for i in range(1,N):
        if S[i-1:i+1] == "AC":
            count[i+1] = count[i] + 1
        else:
            count[i+1] = count[i]
    
    #output
    for i in range(Q):
        print(count[r[i]]-count[l[i]])

=======
Suggestion 10

def main():
    N, Q = map(int, input().split())
    S = input()
    LR = [tuple(map(int, input().split())) for _ in range(Q)]

    # ACが出現する場所を記録
    AC = [0] * N
    for i in range(N - 1):
        if S[i:i + 2] == 'AC':
            AC[i + 1] = 1

    # ACが出現した場所の累積和を求める
    AC_cumsum = [0] * (N + 1)
    for i in range(1, N + 1):
        AC_cumsum[i] = AC_cumsum[i - 1] + AC[i - 1]

    for l, r in LR:
        print(AC_cumsum[r - 1] - AC_cumsum[l - 1])

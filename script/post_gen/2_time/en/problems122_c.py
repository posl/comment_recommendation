Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N, Q = map(int, input().split())
    S = input()
    l = []
    r = []
    for _ in range(Q):
        li, ri = map(int, input().split())
        l.append(li)
        r.append(ri)
    print(N, Q)
    print(S)
    print(l)
    print(r)

=======
Suggestion 2

def main():
    N, Q = map(int, input().split())
    S = input()
    l = [0]
    for i in range(N-1):
        if S[i] == 'A' and S[i+1] == 'C':
            l.append(l[-1] + 1)
        else:
            l.append(l[-1])
    for _ in range(Q):
        l_i, r_i = map(int, input().split())
        print(l[r_i-1] - l[l_i-1])

=======
Suggestion 3

def main():
    n, q = map(int, input().split())
    s = input()
    l = [0] * (n + 1)
    for i in range(n - 1):
        if s[i] == "A" and s[i + 1] == "C":
            l[i + 1] = l[i] + 1
        else:
            l[i + 1] = l[i]
    for _ in range(q):
        a, b = map(int, input().split())
        print(l[b - 1] - l[a - 1])

=======
Suggestion 4

def main():
    n, q = map(int, input().split())
    s = input()
    l = [0] * n
    for i in range(n-1):
        if s[i] == "A" and s[i+1] == "C":
            l[i+1] = l[i] + 1
        else:
            l[i+1] = l[i]
    for i in range(q):
        li, ri = map(int, input().split())
        print(l[ri-1] - l[li-1])

=======
Suggestion 5

def main():
    N, Q = map(int, input().split())
    S = input()
    A = [0] * N
    for i in range(1, N):
        if S[i-1:i+1] == "AC":
            A[i] = A[i-1] + 1
        else:
            A[i] = A[i-1]
    for _ in range(Q):
        l, r = map(int, input().split())
        print(A[r-1] - A[l-1])

main()

=======
Suggestion 6

def main():
    N, Q = map(int, input().split())
    S = input()
    l = [0] * (N + 1)
    for i in range(N):
        if S[i:i+2] == "AC":
            l[i+1] = l[i] + 1
        else:
            l[i+1] = l[i]
    for _ in range(Q):
        l_i, r_i = map(int, input().split())
        print(l[r_i] - l[l_i])

=======
Suggestion 7

def main():
    N,Q = map(int,input().split())
    S = input()
    l = [0]
    for i in range(1,N):
        if S[i-1] == "A" and S[i] == "C":
            l.append(l[i-1]+1)
        else:
            l.append(l[i-1])
    for _ in range(Q):
        l_i,r_i = map(int,input().split())
        print(l[r_i-1]-l[l_i-1])

=======
Suggestion 8

def main():
    N, Q = map(int, input().split())
    S = input()
    lrs = [list(map(int, input().split())) for _ in range(Q)]
    ac = [0] * N
    for i in range(1, N):
        ac[i] = ac[i-1]
        if S[i-1:i+1] == 'AC':
            ac[i] += 1
    for lr in lrs:
        print(ac[lr[1]-1] - ac[lr[0]-1])

=======
Suggestion 9

def main():
    N, Q = map(int, input().split())
    S = input()
    S = S.replace("AC", "X")
    S = S.replace("A", "0")
    S = S.replace("C", "0")
    S = S.replace("G", "0")
    S = S.replace("T", "0")
    S = S.replace("X", "1")
    S = list(map(int, S))
    for i in range(1, N):
        S[i] += S[i - 1]
    for _ in range(Q):
        l, r = map(int, input().split())
        print(S[r - 1] - S[l - 1])

=======
Suggestion 10

def main():
    N, Q = map(int, input().split())
    S = input()
    #N, Q = 8, 3
    #S = 'ACACTACG'
    #lrs = [[3, 7], [2, 3], [1, 8]]
    lrs = [list(map(int, input().split())) for _ in range(Q)]
    #print(N, Q)
    #print(S)
    #print(lrs)
    ac = [0] * N
    for i in range(N - 1):
        if S[i] == 'A' and S[i + 1] == 'C':
            ac[i + 1] = ac[i] + 1
        else:
            ac[i + 1] = ac[i]
    #print(ac)
    for l, r in lrs:
        print(ac[r - 1] - ac[l - 1])

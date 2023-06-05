Synthesizing 10/10 solutions

=======
Suggestion 1

def swap(a, b, s):
    if a < b:
        return s[:a-1] + s[b-1] + s[a:b-1] + s[a-1] + s[b:]
    else:
        return s[:b-1] + s[a-1] + s[b:a-1] + s[b-1] + s[a:]

=======
Suggestion 2

def main():
    N = int(input())
    S = input()
    Q = int(input())
    T = []
    A = []
    B = []
    for i in range(Q):
        t,a,b = map(int,input().split())
        T.append(t)
        A.append(a)
        B.append(b)
    for i in range(Q):
        if T[i] == 1:
            tmp = S[A[i]-1]
            S = S[:A[i]-1] + S[B[i]-1] + S[A[i]:B[i]-1] + tmp + S[B[i]:]
        else:
            S = S[N:] + S[:N]
    print(S)

=======
Suggestion 3

def main():
    n = int(input())
    s = input()
    q = int(input())
    t = [0] * q
    a = [0] * q
    b = [0] * q
    for i in range(q):
        t[i], a[i], b[i] = map(int, input().split())
    # print(n, s, q, t, a, b)
    for i in range(q):
        if t[i] == 1:
            s = s[:a[i]-1] + s[b[i]-1] + s[a[i]:b[i]-1] + s[a[i]-1] + s[b[i]:]
        else:
            s = s[n:] + s[:n]
    print(s)

=======
Suggestion 4

def swap(s, a, b):
    s[a-1], s[b-1] = s[b-1], s[a-1]

=======
Suggestion 5

def main():
    n = int(input())
    s = input()
    q = int(input())
    t = []
    a = []
    b = []
    for i in range(q):
        t1, a1, b1 = map(int, input().split())
        t.append(t1)
        a.append(a1)
        b.append(b1)
    s1 = s[:n]
    s2 = s[n:]
    for i in range(q):
        if t[i] == 1:
            if a[i] < n and b[i] < n:
                s1 = s1[:a[i]] + s2[b[i]] + s1[a[i]+1:]
                s2 = s2[:b[i]] + s1[a[i]] + s2[b[i]+1:]
            elif a[i] < n and b[i] >= n:
                s1 = s1[:a[i]] + s2[b[i]-n] + s1[a[i]+1:]
                s2 = s2[:b[i]-n] + s1[a[i]] + s2[b[i]-n+1:]
            elif a[i] >= n and b[i] < n:
                s1 = s1[:a[i]-n] + s2[b[i]] + s1[a[i]-n+1:]
                s2 = s2[:b[i]] + s1[a[i]-n] + s2[b[i]+1:]
            else:
                s1 = s1[:a[i]-n] + s2[b[i]-n] + s1[a[i]-n+1:]
                s2 = s2[:b[i]-n] + s1[a[i]-n] + s2[b[i]-n+1:]
        else:
            s1, s2 = s2, s1
    print(s1+s2)

=======
Suggestion 6

def main():
    n = int(input())
    s = input()
    q = int(input())
    t = []
    a = []
    b = []
    for i in range(q):
        t_i, a_i, b_i = map(int, input().split())
        t.append(t_i)
        a.append(a_i)
        b.append(b_i)
    for i in range(q):
        if t[i] == 1:
            s = s[:a[i]-1] + s[b[i]-1] + s[a[i]:b[i]-1] + s[a[i]-1] + s[b[i]:]
        elif t[i] == 2:
            s = s[n:] + s[:n]
    print(s)

=======
Suggestion 7

def main():
    N = int(input())
    S = input()
    Q = int(input())
    T = []
    A = []
    B = []
    for i in range(Q):
        t,a,b = map(int, input().split())
        T.append(t)
        A.append(a)
        B.append(b)

    #print("N = ",N)
    #print("S = ",S)
    #print("Q = ",Q)
    #print("T = ",T)
    #print("A = ",A)
    #print("B = ",B)

    for i in range(Q):
        if T[i] == 1:
            #print("交换S的第A_i个和第B_i个字符")
            s = S[A[i]-1]
            S = S[:A[i]-1] + S[B[i]-1] + S[A[i]:B[i]-1] + s + S[B[i]:]
        else:
            #print("交换S的前N个字符和后N个字符")
            S = S[N:] + S[:N]
        #print("S = ",S)

    print(S)

=======
Suggestion 8

def main():
    N = int(input())
    S = input()
    Q = int(input())
    T = []
    A = []
    B = []
    for i in range(Q):
        t, a, b = map(int, input().split())
        T.append(t)
        A.append(a)
        B.append(b)
    for i in range(Q):
        if T[i] == 1:
            if A[i] < N and B[i] < N:
                S = S[:A[i]] + S[B[i]] + S[A[i]+1:B[i]] + S[A[i]] + S[B[i]+1:]
            elif A[i] < N and B[i] >= N:
                S = S[:A[i]] + S[B[i]] + S[A[i]+1:B[i]] + S[A[i]] + S[B[i]+1:]
            elif A[i] >= N and B[i] >= N:
                S = S[:A[i]] + S[B[i]] + S[A[i]+1:B[i]] + S[A[i]] + S[B[i]+1:]
            elif A[i] >= N and B[i] < N:
                S = S[:A[i]] + S[B[i]] + S[A[i]+1:B[i]] + S[A[i]] + S[B[i]+1:]
        elif T[i] == 2:
            S = S[N:] + S[:N]
    print(S)

=======
Suggestion 9

def solve():
    n = int(input())
    s = input()
    q = int(input())
    t = []
    a = []
    b = []
    for i in range(q):
        t_i, a_i, b_i = map(int, input().split())
        t.append(t_i)
        a.append(a_i)
        b.append(b_i)
    t.reverse()
    a.reverse()
    b.reverse()
    s = list(s)
    for i in range(q):
        if t[i] == 1:
            s[a[i]-1], s[b[i]-1] = s[b[i]-1], s[a[i]-1]
        else:
            s[:n], s[n:] = s[n:], s[:n]
    print("".join(s))

=======
Suggestion 10

def solve():
    n = int(input())
    s = input()
    q = int(input())
    t = []
    a = []
    b = []
    for i in range(q):
        tmp = input().split()
        t.append(int(tmp[0]))
        a.append(int(tmp[1]))
        b.append(int(tmp[2]))
    isFront = True
    for i in range(q-1, -1, -1):
        if t[i] == 1:
            if isFront:
                if a[i] <= n and b[i] <= n:
                    s = s[:a[i]-1] + s[b[i]-1] + s[a[i]:b[i]-1] + s[a[i]-1] + s[b[i]:]
                elif a[i] <= n and n < b[i]:
                    s = s[:a[i]-1] + s[b[i]-1] + s[a[i]:n] + s[n-1] + s[n:b[i]-1] + s[a[i]-1] + s[b[i]:]
                elif n < a[i] and b[i] <= 2*n:
                    s = s[:n] + s[a[i]-1-n] + s[n:a[i]-1] + s[b[i]-1-n] + s[a[i]-1:b[i]-1] + s[b[i]-n:]
                elif n < a[i] and 2*n < b[i]:
                    s = s[:n] + s[a[i]-1-n] + s[n:a[i]-1] + s[b[i]-1-n] + s[a[i]-1:n] + s[b[i]-1] + s[n:b[i]-n-1] + s[b[i]-n:]
            else:
                if a[i] <= n and b[i] <= n:
                    s = s[:a[i]-1+n] + s[b[i]-1+n] + s[a[i]-1+n+1:b[i]-1+n] + s[a[i]-1+n] + s[b[i]-1+n+1:]
                elif a[i] <= n and n < b[i]:
                    s = s[:a[i]-1+n] + s[b[i]-1] + s[a[i]-1+n+1:n] + s[b[i]-1+n] + s[a[i]-1:n-1] + s[b[i]-1

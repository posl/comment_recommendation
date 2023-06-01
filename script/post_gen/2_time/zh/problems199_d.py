Synthesizing 10/10 solutions

=======
Suggestion 1

def swap(s, a, b):
    s[a-1], s[b-1] = s[b-1], s[a-1]

=======
Suggestion 2

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
    # print(t)
    # print(a)
    # print(b)
    s1 = s[:n]
    s2 = s[n:]
    for i in range(q):
        if t[i] == 1:
            if a[i] <= n and b[i] <= n:
                s1 = s1[:a[i]-1] + s2[b[i]-1] + s1[a[i]:]
                s2 = s2[:b[i]-1] + s1[a[i]-1] + s2[b[i]:]
            elif a[i] <= n and b[i] > n:
                s1 = s1[:a[i]-1] + s2[b[i]-n-1] + s1[a[i]:]
                s2 = s2[:b[i]-n-1] + s1[a[i]-1] + s2[b[i]-n:]
            elif a[i] > n and b[i] <= n:
                s1 = s1[:a[i]-n-1] + s2[b[i]-1] + s1[a[i]-n:]
                s2 = s2[:b[i]-1] + s1[a[i]-n-1] + s2[b[i]:]
            else:
                s1 = s1[:a[i]-n-1] + s2[b[i]-n-1] + s1[a[i]-n:]
                s2 = s2[:b[i]-n-1] + s1[a[i]-n-1] + s2[b[i]-n:]
        else:
            s1, s2 = s2, s1
    print(s1 + s2)

solve()

=======
Suggestion 3

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
            S = S[:A[i]-1] + S[B[i]-1] + S[A[i]:B[i]-1] + S[A[i]-1] + S[B[i]:]
        elif T[i] == 2:
            S = S[N:] + S[:N]
    print(S)

=======
Suggestion 4

def swap(s, a, b):
    return s[:a-1] + s[b-1] + s[a:b-1] + s[a-1] + s[b:]

=======
Suggestion 5

def main():
    N = int(input())
    S = input()
    Q = int(input())
    T = []
    A = []
    B = []
    for i in range(Q):
        t, a, b = input().split()
        T.append(int(t))
        A.append(int(a))
        B.append(int(b))
    for i in range(Q):
        if T[i] == 1:
            S = S[:A[i]-1] + S[B[i]-1] + S[A[i]:B[i]-1] + S[A[i]-1] + S[B[i]:]
        else:
            S = S[N:] + S[:N]
    print(S)

=======
Suggestion 6

def solve():
    n = int(input())
    s = input()
    q = int(input())

    # 0-indexed
    # 前半部分
    s1 = s[:n]
    # 后半部分
    s2 = s[n:]

    # 1-indexed
    # 前半部分
    s1 = list(s1)
    # 后半部分
    s2 = list(s2)

    for _ in range(q):
        t, a, b = map(int, input().split())
        if t == 1:
            a -= 1
            b -= 1
            if a < n and b < n:
                s1[a], s1[b] = s1[b], s1[a]
            elif a < n and b >= n:
                b -= n
                s1[a], s2[b] = s2[b], s1[a]
            elif a >= n and b >= n:
                a -= n
                b -= n
                s2[a], s2[b] = s2[b], s2[a]
        elif t == 2:
            s1, s2 = s2, s1
    print(''.join(s1) + ''.join(s2))

=======
Suggestion 7

def main():
    n = int(input())
    s = input()
    q = int(input())
    t = []
    a = []
    b = []
    for i in range(q):
        tt, aa, bb = map(int, input().split())
        t.append(tt)
        a.append(aa)
        b.append(bb)
    #print(t)
    #print(a)
    #print(b)
    #print(s)
    for i in range(q):
        if t[i] == 1:
            if a[i] <= n:
                aa = a[i] - 1
            else:
                aa = a[i] - 1 - n
            if b[i] <= n:
                bb = b[i] - 1
            else:
                bb = b[i] - 1 - n
            ss = s[aa]
            s = s[:aa] + s[bb] + s[aa+1:]
            s = s[:bb] + ss + s[bb+1:]
        else:
            ss = s[:n]
            s = s[n:] + ss
        #print(s)
    print(s)

=======
Suggestion 8

def main():
    n = int(input())
    s = input()
    q = int(input())
    t = []
    a = []
    b = []
    for i in range(q):
        ti, ai, bi = map(int, input().split())
        t.append(ti)
        a.append(ai)
        b.append(bi)

    for i in range(q):
        if t[i] == 1:
            s = s[:a[i]-1] + s[b[i]-1] + s[a[i]:b[i]-1] + s[a[i]-1] + s[b[i]:]
        else:
            s = s[n:] + s[:n]

    print(s)

=======
Suggestion 9

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
    flag = 0
    S1 = S[:N]
    S2 = S[N:]
    for i in range(Q):
        if T[i] == 1:
            if flag == 0:
                if A[i] <= N and B[i] <= N:
                    S1 = S1[:A[i]-1] + S2[B[i]-1] + S1[A[i]:]
                    S2 = S2[:B[i]-1] + S[S1.index(S2[B[i]-1])] + S2[B[i]:]
                elif A[i] > N and B[i] > N:
                    S2 = S2[:A[i]-N-1] + S1[B[i]-N-1] + S2[A[i]-N:]
                    S1 = S1[:B[i]-N-1] + S[S2.index(S1[B[i]-N-1])] + S1[B[i]-N:]
                elif A[i] <= N and B[i] > N:
                    S1 = S1[:A[i]-1] + S2[B[i]-N-1] + S1[A[i]:]
                    S2 = S2[:B[i]-N-1] + S[S1.index(S2[B[i]-N-1])] + S2[B[i]-N:]
                elif A[i] > N and B[i] <= N:
                    S2 = S2[:A[i]-N-1] + S1[B[i]-1] + S2[A[i]-N:]
                    S1 = S1[:B[i]-1] + S[S2.index(S1[B[i]-1])] + S1[B[i]:]
            else:
                if A[i] <= N and B[i] <= N:
                    S2 = S2[:A[i]-1] + S1[B[i]-1] + S2[A[i]:]
                    S1 = S1[:B[i]-1] + S[S2.index(S1[B[i]-1])] + S1[B[i]:]
                elif A[i] >

=======
Suggestion 10

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
        t = T[i]
        a = A[i]
        b = B[i]
        if t == 1:
            S = S[:a-1] + S[b-1] + S[a:b-1] + S[a-1] + S[b:]
        elif t == 2:
            S = S[N:] + S[:N]
    print(S)

Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N = int(input())
    S = input()
    Q = int(input())
    T = []
    A = []
    B = []
    for i in range(Q):
        T_i, A_i, B_i = map(int, input().split())
        T.append(T_i)
        A.append(A_i)
        B.append(B_i)
    
    S = list(S)
    for i in range(Q):
        if T[i] == 1:
            S[A[i]-1], S[B[i]-1] = S[B[i]-1], S[A[i]-1]
        else:
            S[:N], S[N:] = S[N:], S[:N]
    print(''.join(S))

=======
Suggestion 2

def main():
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

    for i in range(q):
        if t[i] == 1:
            if a[i] <= n and b[i] <= n:
                s = s[:a[i]-1] + s[b[i]-1] + s[a[i]:b[i]-1] + s[a[i]-1] + s[b[i]:]
            elif a[i] <= n and b[i] > n:
                s = s[:a[i]-1] + s[b[i]-1] + s[a[i]:n] + s[n:b[i]-1] + s[a[i]-1] + s[b[i]:]
            elif a[i] > n and b[i] <= n:
                s = s[:n] + s[a[i]-1] + s[n+1:b[i]-1] + s[a[i]-1] + s[b[i]:]
            elif a[i] > n and b[i] > n:
                s = s[:n] + s[a[i]-1] + s[n+1:n] + s[b[i]-1] + s[n+1:a[i]-1] + s[b[i]-1] + s[a[i]:]
        elif t[i] == 2:
            s = s[n:] + s[:n]
    print(s)

=======
Suggestion 3

def main():
    N = int(input())
    S = input()
    Q = int(input())
    T = [0] * Q
    A = [0] * Q
    B = [0] * Q
    for i in range(Q):
        T[i], A[i], B[i] = map(int, input().split())
    head = S[:N]
    tail = S[N:]
    for i in range(Q):
        if T[i] == 1:
            if A[i] <= N:
                if B[i] <= N:
                    head = head[:A[i]-1] + tail[B[i]-1] + head[A[i]:]
                    tail = tail[:B[i]-1] + head[A[i]-1] + tail[B[i]:]
                else:
                    head = head[:A[i]-1] + tail[B[i]-N-1] + head[A[i]:]
                    tail = tail[:B[i]-N-1] + head[A[i]-1] + tail[B[i]-N:]
            else:
                if B[i] <= N:
                    head = head[:A[i]-N-1] + tail[B[i]-1] + head[A[i]-N:]
                    tail = tail[:B[i]-1] + head[A[i]-N-1] + tail[B[i]:]
                else:
                    head = head[:A[i]-N-1] + tail[B[i]-N-1] + head[A[i]-N:]
                    tail = tail[:B[i]-N-1] + head[A[i]-N-1] + tail[B[i]-N:]
        else:
            head, tail = tail, head
    print(head + tail)

=======
Suggestion 4

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
            if a[i] > n:
                a[i] -= n
            else:
                a[i] += n
            if b[i] > n:
                b[i] -= n
            else:
                b[i] += n
            s = s[:a[i]-1] + s[b[i]-1] + s[a[i]:b[i]-1] + s[a[i]-1] + s[b[i]:]
        else:
            s = s[n:] + s[:n]
    print(s)

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
        t, a, b = map(int, input().split())
        T.append(t)
        A.append(a)
        B.append(b)

    for i in range(Q):
        if T[i] == 1:
            if A[i] > N:
                a = A[i] - N
            else:
                a = A[i] + N
            if B[i] > N:
                b = B[i] - N
            else:
                b = B[i] + N
            S = S[:a-1] + S[b-1] + S[a:b-1] + S[a-1] + S[b:]
        else:
            S = S[N:] + S[:N]
    print(S)

=======
Suggestion 6

def swap(s, a, b):
    temp = s[a-1]
    s[a-1] = s[b-1]
    s[b-1] = temp

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
        t, a, b = map(int, input().split())
        T.append(t)
        A.append(a)
        B.append(b)
    for i in range(Q):
        if T[i] == 1:
            S = S[:A[i]-1] + S[B[i]-1] + S[A[i]:B[i]-1] + S[A[i]-1] + S[B[i]:]
        else:
            S = S[N:] + S[:N]
    print(S)

=======
Suggestion 8

def main():
    N = int(input())
    S = list(input())
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
            S[A[i]-1], S[B[i]-1] = S[B[i]-1], S[A[i]-1]
        elif T[i] == 2:
            S = S[N:] + S[:N]
    print(''.join(S))

=======
Suggestion 9

def main():
    N = int(input())
    S = input()
    Q = int(input())
    T = [0]*Q
    A = [0]*Q
    B = [0]*Q
    for i in range(Q):
        T[i], A[i], B[i] = map(int, input().split())
    #print(N, S, Q, T, A, B)
    for i in range(Q):
        if T[i] == 1:
            S = S[:A[i]-1] + S[B[i]-1] + S[A[i]:B[i]-1] + S[A[i]-1] + S[B[i]:]
        else:
            S = S[N:] + S[:N]
    print(S)

=======
Suggestion 10

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
    #print(t)
    #print(a)
    #print(b)
    #print(s)
    s1 = s[:n]
    s2 = s[n:]
    for i in range(q):
        if t[i] == 1:
            if a[i] <= n and b[i] <= n:
                s1 = s1[:a[i]-1] + s2[b[i]-1] + s1[a[i]:]
                s2 = s2[:b[i]-1] + s1[a[i]-1] + s2[b[i]:]
            elif a[i] > n and b[i] > n:
                s2 = s2[:a[i]-n-1] + s1[b[i]-n-1] + s2[a[i]-n:]
                s1 = s1[:b[i]-n-1] + s2[a[i]-n-1] + s1[b[i]-n:]
            else:
                s1 = s1[:a[i]-1] + s2[b[i]-n-1] + s1[a[i]:]
                s2 = s2[:b[i]-n-1] + s1[a[i]-1] + s2[b[i]-n:]
        else:
            s1, s2 = s2, s1
    print(s1 + s2)

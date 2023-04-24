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
        t, a, b = map(int, input().split())
        T.append(t)
        A.append(a)
        B.append(b)
    #print(N)
    #print(S)
    #print(Q)
    #print(T)
    #print(A)
    #print(B)
    for i in range(Q):
        if T[i] == 1:
            a = S[A[i]-1]
            b = S[B[i]-1]
            S = S[:A[i]-1] + b + S[A[i]:B[i]-1] + a + S[B[i]:]
        else:
            S = S[N:] + S[:N]
    print(S)

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
        t, a, b = map(int, input().split())
        T.append(t)
        A.append(a)
        B.append(b)
    #print(N)
    #print(S)
    #print(Q)
    #print(T)
    #print(A)
    #print(B)

    s1 = S[0:N]
    s2 = S[N:2*N]
    #print(s1)
    #print(s2)

    for i in range(Q):
        if T[i] == 1:
            if A[i] > N:
                A[i] -= N
            else:
                A[i] += N
            if B[i] > N:
                B[i] -= N
            else:
                B[i] += N
            #print(A[i])
            #print(B[i])
            #print(s1)
            #print(s2)
            if A[i] > B[i]:
                tmp = A[i]
                A[i] = B[i]
                B[i] = tmp
            if A[i] == 1:
                s1 = s2[B[i]-2] + s1[1:A[i]-1] + s2[A[i]-2] + s1[A[i]:N]
                s2 = s2[0:B[i]-1] + s1[B[i]-2] + s2[B[i]:N]
            else:
                s1 = s1[0:A[i]-1] + s2[A[i]-2] + s1[A[i]:N]
                s2 = s1[B[i]-2] + s2[A[i]:B[i]-1] + s1[B[i]-2] + s2[B[i]:N]
            #print(s1)
            #print(s2)
        else:
            tmp = s1
            s1 = s2
            s2 = tmp
            #print(s1)
            #print(s2)

    print(s1 + s2)

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

    a = list(S[:N])
    b = list(S[N:])

    for i in range(Q):
        if T[i] == 1:
            if A[i] <= N:
                a[A[i]-1], a[B[i]-1] = a[B[i]-1], a[A[i]-1]
            else:
                b[A[i]-N-1], b[B[i]-N-1] = b[B[i]-N-1], b[A[i]-N-1]
        elif T[i] == 2:
            a, b = b, a

    print("".join(a+b))

=======
Suggestion 4

def solve():
    N = int(input())
    S = input()
    Q = int(input())
    T = [0] * Q
    A = [0] * Q
    B = [0] * Q
    for i in range(Q):
        T[i], A[i], B[i] = map(int, input().split())

    #print(N, S, Q, T, A, B)

    S1 = S[0:N]
    S2 = S[N:2*N]

    #print(S1, S2)

    for i in range(Q):
        if T[i] == 2:
            S1, S2 = S2, S1
        else:
            if A[i] - 1 < N:
                if B[i] - 1 < N:
                    S1 = S1[0:A[i]-1] + S2[B[i]-1] + S1[A[i]:B[i]-1] + S2[A[i]-1] + S1[B[i]:]
                else:
                    S1 = S1[0:A[i]-1] + S2[A[i]-1] + S1[A[i]:]
                    S2 = S2[0:B[i]-N-1] + S1[B[i]-N-1] + S2[B[i]-N:B[i]-1] + S1[B[i]-1] + S2[B[i]:]
            else:
                S2 = S2[0:A[i]-N-1] + S1[A[i]-N-1] + S2[A[i]-N:A[i]-1] + S1[A[i]-1] + S2[A[i]:]
                S1 = S1[0:B[i]-1] + S2[B[i]-1] + S1[B[i]:]

        #print(S1, S2)

    print(S1 + S2)

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
        t,a,b = map(int,input().split())
        T.append(t)
        A.append(a)
        B.append(b)
    for i in range(Q):
        if T[i] == 1:
            if A[i] > N:
                A[i] -= N
            elif A[i] <= N:
                A[i] += N
            if B[i] > N:
                B[i] -= N
            elif B[i] <= N:
                B[i] += N
            S = S[:A[i]-1] + S[B[i]-1] + S[A[i]:B[i]-1] + S[A[i]-1] + S[B[i]:]
        elif T[i] == 2:
            S = S[N:] + S[:N]
    print(S)

=======
Suggestion 6

def solve():
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
    
    S = list(S)
    for i in range(Q):
        if T[i] == 1:
            S[A[i]-1], S[B[i]-1] = S[B[i]-1], S[A[i]-1]
        elif T[i] == 2:
            S[:N], S[N:] = S[N:], S[:N]
    print(''.join(S))

=======
Suggestion 7

def main():
    n = int(input())
    s = input()
    q = int(input())
    s1 = list(s[:n])
    s2 = list(s[n:])
    for i in range(q):
        t, a, b = map(int, input().split())
        if t == 1:
            if a <= n and b <= n:
                s1[a-1], s1[b-1] = s1[b-1], s1[a-1]
            elif a <= n and b > n:
                s1[a-1], s2[b-n-1] = s2[b-n-1], s1[a-1]
            elif a > n and b <= n:
                s2[a-n-1], s1[b-1] = s1[b-1], s2[a-n-1]
            else:
                s2[a-n-1], s2[b-n-1] = s2[b-n-1], s2[a-n-1]
        else:
            s1, s2 = s2, s1
    print("".join(s1+s2))

=======
Suggestion 8

def main():
    n = int(input())
    s = input()
    q = int(input())
    t, a, b = [], [], []
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
    n = int(input())
    s = input()
    q = int(input())
    t = []
    a = []
    b = []
    for i in range(q):
        t_temp, a_temp, b_temp = map(int, input().split())
        t.append(t_temp)
        a.append(a_temp)
        b.append(b_temp)
    s = list(s)
    for i in range(q):
        if t[i] == 1:
            s[a[i]-1], s[b[i]-1] = s[b[i]-1], s[a[i]-1]
        else:
            s[:n], s[n:] = s[n:], s[:n]
    print(''.join(s))

=======
Suggestion 10

def reverse(s):
    return s[::-1]

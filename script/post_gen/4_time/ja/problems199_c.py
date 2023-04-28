Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N = int(input())
    S = input()
    Q = int(input())
    T = [0] * Q
    A = [0] * Q
    B = [0] * Q
    for i in range(Q):
        T[i], A[i], B[i] = map(int, input().split())
    for i in range(Q):
        if T[i] == 1:
            if A[i] <= N:
                if B[i] <= N:
                    S = S[:A[i]-1] + S[B[i]-1] + S[A[i]:B[i]-1] + S[A[i]-1] + S[B[i]:]
                else:
                    S = S[:A[i]-1] + S[B[i]-1] + S[A[i]:N] + S[A[i]-1] + S[N:B[i]-1] + S[B[i]:]
            else:
                if B[i] <= N:
                    S = S[:N] + S[A[i]-1] + S[N+1:B[i]-1] + S[A[i]-1] + S[B[i]:]
                else:
                    S = S[:N] + S[A[i]-1] + S[N+1:N] + S[A[i]-1] + S[N:B[i]-1] + S[B[i]:]
        else:
            S = S[N:] + S[:N]
    print(S)

=======
Suggestion 2

def main():
    N = int(input())
    S = input()
    Q = int(input())
    T = [0] * Q
    A = [0] * Q
    B = [0] * Q
    for i in range(Q):
        T[i], A[i], B[i] = map(int, input().split())
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
            S = S[:A[i]-1] + S[B[i]-1] + S[A[i]:B[i]-1] + S[A[i]-1] + S[B[i]:]
        else:
            S = S[N:] + S[:N]
    print(S)

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
    is_reverse = False
    for i in range(Q):
        if T[i] == 1:
            if is_reverse:
                a = A[i] + N if A[i] <= N else A[i] - N
                b = B[i] + N if B[i] <= N else B[i] - N
                S = S[:a-1] + S[b-1] + S[a:b-1] + S[a-1] + S[b:]
            else:
                S = S[:A[i]-1] + S[B[i]-1] + S[A[i]:B[i]-1] + S[A[i]-1] + S[B[i]:]
        else:
            is_reverse = not is_reverse
    if is_reverse:
        S = S[N:] + S[:N]
    print(S)

=======
Suggestion 4

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
    #print(N,S,Q,T,A,B)
    for i in range(Q):
        if T[i] == 1:
            a = A[i] - 1
            b = B[i] - 1
            #print("a,b",a,b)
            s = list(S)
            #print(s)
            s[a],s[b] = s[b],s[a]
            S = "".join(s)
            #print(S)
        elif T[i] == 2:
            #print("2")
            s = list(S)
            s[:N],s[N:] = s[N:],s[:N]
            S = "".join(s)
            #print(S)
    print(S)
main()

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
        t,a,b = map(int, input().split())
        T.append(t)
        A.append(a)
        B.append(b)
    
    #print(T)
    #print(A)
    #print(B)

    #print(S[:N])
    #print(S[N:])

    for i in range(Q):
        if T[i] == 1:
            if A[i] <= N:
                a = A[i] - 1
            else:
                a = A[i] - N - 1
            if B[i] <= N:
                b = B[i] - 1
            else:
                b = B[i] - N - 1
            #print(a,b)
            S = S[:a] + S[b] + S[a+1:b] + S[a] + S[b+1:]
        else:
            S = S[N:] + S[:N]
        #print(S[:N])
        #print(S[N:])
    print(S)

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
        ti, ai, bi = map(int, input().split())
        t.append(ti)
        a.append(ai)
        b.append(bi)

    for i in range(q):
        if t[i] == 1:
            s = s[:a[i]-1] + s[b[i]-1] + s[a[i]:b[i]-1] + s[a[i]-1] + s[b[i]:]
        elif t[i] == 2:
            s = s[n:] + s[:n]

    print(s)

=======
Suggestion 7

def main():
    n = int(input())
    s = input()
    q = int(input())

    s1 = s[:n]
    s2 = s[n:]

    for i in range(q):
        t, a, b = map(int, input().split())
        if t == 1:
            if a <= n and b <= n:
                s1 = s1[:a-1] + s2[b-1] + s1[a:b-1] + s2[a-1] + s1[b:]
            elif n < a and n < b:
                s2 = s2[:a-n-1] + s1[b-n-1] + s2[a-n:b-n-1] + s1[a-n-1] + s2[b-n:]
            elif n < a and b <= n:
                s2 = s2[:a-n-1] + s2[b-1] + s2[a-n:b-1] + s2[a-n-1] + s2[b:]
            elif a <= n and n < b:
                s1 = s1[:a-1] + s1[b-n-1] + s1[a:b-n-1] + s1[a-1] + s1[b-n:]
        elif t == 2:
            s1, s2 = s2, s1

    print(s1 + s2)

=======
Suggestion 8

def main():
    N = int(input())
    S = input()
    Q = int(input())

    T = [0]*Q
    A = [0]*Q
    B = [0]*Q

    for i in range(Q):
        T[i], A[i], B[i] = map(int, input().split())

    for i in range(Q):
        if T[i] == 1:
            if A[i] <= N:
                if B[i] <= N:
                    S = S[:A[i]-1] + S[B[i]-1] + S[A[i]:B[i]-1] + S[A[i]-1] + S[B[i]:]
                else:
                    S = S[:A[i]-1] + S[B[i]-1] + S[A[i]:N] + S[A[i]-1] + S[N:B[i]-1] + S[B[i]:]
            else:
                if B[i] <= N:
                    S = S[:N] + S[A[i]-1] + S[N:B[i]-1] + S[A[i]:N] + S[B[i]:]
                else:
                    S = S[:N] + S[A[i]-1] + S[N:B[i]-1] + S[A[i]:N] + S[B[i]:]

        else:
            S = S[N:] + S[:N]

    print(S)

=======
Suggestion 9

def swap(s, a, b):
    s = list(s)
    tmp = s[a-1]
    s[a-1] = s[b-1]
    s[b-1] = tmp
    return "".join(s)

=======
Suggestion 10

def main():
    n = int(input())
    s = input()
    q = int(input())
    s = list(s)
    f = 0
    for i in range(q):
        t, a, b = map(int, input().split())
        if t == 1:
            if f == 1:
                if a > n:
                    a -= n
                else:
                    a += n
                if b > n:
                    b -= n
                else:
                    b += n
            s[a-1], s[b-1] = s[b-1], s[a-1]
        else:
            f = 1 - f
    if f == 1:
        s = s[n:] + s[:n]
    print("".join(s))

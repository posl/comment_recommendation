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
    flip = False
    for i in range(Q):
        if T[i] == 1:
            if flip:
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
            flip = not flip
    if flip:
        print(S[N:] + S[:N])
    else:
        print(S)

main()

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
    ans = ''
    for i in range(Q):
        if T[i] == 1:
            if A[i] > N:
                A[i] = A[i] - N
            elif A[i] <= N:
                A[i] = A[i] + N
            if B[i] > N:
                B[i] = B[i] - N
            elif B[i] <= N:
                B[i] = B[i] + N
            S = S[:A[i]-1] + S[B[i]-1] + S[A[i]:B[i]-1] + S[A[i]-1] + S[B[i]:]
        elif T[i] == 2:
            S = S[N:] + S[:N]
    ans = S
    print(ans)

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

    # swap 1st half and 2nd half
    swap = False
    
    for i in range(Q):
        if T[i] == 1:
            if swap:
                a = A[i] - N
                b = B[i] - N
                if a < 0:
                    a += 2*N
                if b < 0:
                    b += 2*N
                A[i] = a
                B[i] = b
            S = S[:A[i]-1] + S[B[i]-1] + S[A[i]:B[i]-1] + S[A[i]-1] + S[B[i]:]
        else:
            swap = not swap

    if swap:
        print(S[N:] + S[:N])
    else:
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
        t, a, b = map(int, input().split())
        T.append(t)
        A.append(a)
        B.append(b)
    #print(N, S, Q, T, A, B)
    #print((N, S, Q, T, A, B))
    #print((N, S, Q, T, A, B), file=sys.stderr)
    #print((N, S, Q, T, A, B), file=sys.stderr, flush=True)
    #print((N, S, Q, T, A, B), file=sys.stderr, end="

")
    #print((N, S, Q, T, A, B), file=sys.stderr, end="

", flush=True)
    #print((N, S, Q, T, A, B), file=sys.stderr, sep=" ")
    #print((N, S, Q, T, A, B), file=sys.stderr, sep=" ", flush=True)
    #print((N, S, Q, T, A, B), file=sys.stderr, sep=" ", end="

")
    #print((N, S, Q, T, A, B), file=sys.stderr, sep=" ", end="

", flush=True)
    #print((N, S, Q, T, A, B), file=sys.stdout)
    #print((N, S, Q, T, A, B), file=sys.stdout, flush=True)
    #print((N, S, Q, T, A, B), file=sys.stdout, end="

")
    #print((N, S, Q, T, A, B), file=sys.stdout, end="

", flush=True)
    #print((N, S, Q, T, A, B), file=sys.stdout, sep=" ")
    #print((N, S, Q, T, A, B), file=sys.stdout, sep=" ", flush=True)
    #print((N, S, Q, T, A, B), file=sys.stdout, sep=" ", end="

")
    #print((N, S, Q, T, A, B), file=sys.stdout, sep=" ", end="

", flush=True)
    #

=======
Suggestion 5

def main():
    n = int(input())
    s = list(input())
    q = int(input())
    for _ in range(q):
        t, a, b = map(int, input().split())
        if t == 1:
            s[a-1], s[b-1] = s[b-1], s[a-1]
        else:
            s = s[n:] + s[:n]
    print("".join(s))

=======
Suggestion 6

def main():
    N = int(input())
    S = input()
    Q = int(input())
    T = [0 for i in range(Q)]
    A = [0 for i in range(Q)]
    B = [0 for i in range(Q)]
    for i in range(Q):
        T[i], A[i], B[i] = map(int, input().split())
    S = list(S)
    #print(S)
    #print(T)
    #print(A)
    #print(B)
    #print(N)
    #print(Q)
    flag = 0
    for i in range(Q):
        if T[i] == 1:
            if flag == 0:
                S[A[i]-1], S[B[i]-1] = S[B[i]-1], S[A[i]-1]
            else:
                if A[i] <= N:
                    A[i] = A[i] + N
                else:
                    A[i] = A[i] - N
                if B[i] <= N:
                    B[i] = B[i] + N
                else:
                    B[i] = B[i] - N
                S[A[i]-1], S[B[i]-1] = S[B[i]-1], S[A[i]-1]
        else:
            if flag == 0:
                flag = 1
            else:
                flag = 0
    if flag == 1:
        S = S[N:] + S[:N]
    print(''.join(S))

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
        t_i, a_i, b_i = map(int, input().split())
        t.append(t_i)
        a.append(a_i)
        b.append(b_i)
    s1 = s[:n]
    s2 = s[n:]
    for i in range(q):
        if t[i] == 2:
            s1, s2 = s2, s1
        else:
            if a[i] <= n:
                if b[i] <= n:
                    s1 = s1[:a[i] - 1] + s1[b[i] - 1] + s1[a[i]:b[i] - 1] + s1[a[i] - 1] + s1[b[i]:]
                else:
                    s1 = s1[:a[i] - 1] + s2[b[i] - n - 1] + s1[a[i]:]
                    s2 = s2[:b[i] - n - 1] + s1[a[i] - 1] + s2[b[i] - n:]
            else:
                if b[i] <= n:
                    s2 = s2[:a[i] - n - 1] + s1[b[i] - 1] + s2[a[i] - n:]
                    s1 = s1[:b[i] - 1] + s2[a[i] - n - 1] + s1[b[i]:]
                else:
                    s2 = s2[:a[i] - n - 1] + s2[b[i] - n - 1] + s2[a[i] - n:b[i] - n - 1] + s2[a[i] - n - 1] + s2[b[i] - n:]
    print(s1 + s2)

main()

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
        t_i, a_i, b_i = map(int, input().split())
        t.append(t_i)
        a.append(a_i)
        b.append(b_i)
    s = list(s)
    for i in range(q):
        if t[i] == 1:
            s[a[i]-1], s[b[i]-1] = s[b[i]-1], s[a[i]-1]
        else:
            s = s[n:] + s[:n]
    print(''.join(s))

=======
Suggestion 9

def main():
    N = int(input())
    S = input()
    Q = int(input())
    S1 = S[:N]
    S2 = S[N:]
    for _ in range(Q):
        T, A, B = map(int, input().split())
        if T == 1:
            if A <= N and B <= N:
                S1 = swap(S1, A-1, B-1)
            elif A > N and B > N:
                S2 = swap(S2, A-1-N, B-1-N)
            else:
                S1 = swap(S1, A-1, B-1-N)
                S2 = swap(S2, A-1-N, B-1)
        else:
            S1, S2 = S2, S1
    print(S1+S2)

=======
Suggestion 10

def main():
    N = int(input())
    S = input()
    Q = int(input())
    #T, A, B = [int(x) for x in input().split()]

Synthesizing 10/10 solutions

=======
Suggestion 1

def flip(s, a, b):
    return s[:a-1] + s[b-1] + s[a:b-1] + s[a-1] + s[b:]

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
        t,a,b = map(int, input().split())
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
Suggestion 3

def main():
    n = int(input())
    s = input()
    q = int(input())
    s = list(s)
    for i in range(q):
        t, a, b = map(int, input().split())
        if t == 1:
            a -= 1
            b -= 1
            s[a], s[b] = s[b], s[a]
        else:
            s[:n], s[n:] = s[n:], s[:n]
    print(''.join(s))

=======
Suggestion 4

def main():
    # input
    N = int(input())
    S = input()
    Q = int(input())
    TABs = [list(map(int, input().split())) for _ in range(Q)]

    # compute
    S = list(S)
    for TAB in TABs:
        if TAB[0] == 1:
            S[TAB[1]-1], S[TAB[2]-1] = S[TAB[2]-1], S[TAB[1]-1]
        else:
            S[:N], S[N:] = S[N:], S[:N]

    # output
    print(''.join(S))

=======
Suggestion 5

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
    #print(N, S, Q, T, A, B)
    S1 = S[:N]
    S2 = S[N:]
    #print(S1, S2)
    for i in range(Q):
        if T[i] == 1:
            if A[i] <= N:
                S1 = S1[:A[i]-1] + S2[B[i]-1] + S1[A[i]:]
            elif A[i] > N:
                S2 = S2[:A[i]-N-1] + S1[B[i]-1] + S2[A[i]-N:]
        elif T[i] == 2:
            S1, S2 = S2, S1
        #print(S1, S2)
    print(S1+S2)
main()

=======
Suggestion 6

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

    is_front = True
    for i in range(Q):
        if T[i] == 1:
            if is_front:
                S = S[:A[i] - 1] + S[B[i] - 1] + S[A[i]:B[i] - 1] + S[A[i] - 1] + S[B[i]:]
            else:
                if A[i] <= N:
                    A[i] = A[i] + N
                else:
                    A[i] = A[i] - N
                if B[i] <= N:
                    B[i] = B[i] + N
                else:
                    B[i] = B[i] - N
                S = S[:A[i] - 1] + S[B[i] - 1] + S[A[i]:B[i] - 1] + S[A[i] - 1] + S[B[i]:]
        else:
            is_front = not is_front
    if not is_front:
        S = S[N:] + S[:N]
    print(S)

=======
Suggestion 7

def main():
    n = int(input())
    s = input()
    q = int(input())
    s = list(s)
    for i in range(q):
        t,a,b = map(int, input().split())
        a -= 1
        b -= 1
        if t == 1:
            s[a],s[b] = s[b],s[a]
        else:
            s = s[n:] + s[:n]
    print("".join(s))

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

    S1 = S[:N]
    S2 = S[N:]
    for i in range(Q):
        if T[i] == 1:
            if A[i] <= N:
                S1 = S1[:A[i]-1] + S2[B[i]-N-1] + S1[A[i]:]
            else:
                S2 = S2[:A[i]-N-1] + S1[B[i]-1] + S2[A[i]-N:]
        else:
            S1, S2 = S2, S1
    print(S1+S2)

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

    #print(N)
    #print(S)
    #print(Q)
    #print(T)
    #print(A)
    #print(B)

    S1 = S[:N]
    S2 = S[N:]

    for i in range(Q):
        if T[i] == 1:
            if A[i] < N and B[i] < N:
                tmp = S1[A[i]]
                S1 = S1[:A[i]] + S1[B[i]] + S1[A[i]+1:]
                S1 = S1[:B[i]] + tmp + S1[B[i]+1:]
            elif A[i] < N and B[i] >= N:
                tmp = S1[A[i]]
                S1 = S1[:A[i]] + S2[B[i]-N] + S1[A[i]+1:]
                S2 = S2[:B[i]-N] + tmp + S2[B[i]-N+1:]
            elif A[i] >= N and B[i] < N:
                tmp = S2[A[i]-N]
                S2 = S2[:A[i]-N] + S1[B[i]] + S2[A[i]-N+1:]
                S1 = S1[:B[i]] + tmp + S1[B[i]+1:]
            elif A[i] >= N and B[i] >= N:
                tmp = S2[A[i]-N]
                S2 = S2[:A[i]-N] + S2[B[i]-N] + S2[A[i]-N+1:]
                S2 = S2[:B[i]-N] + tmp + S2[B[i]-N+1:]
        elif T[i] == 2:
            S1, S2 = S2, S1

    S = S1 + S2
    print(S)

=======
Suggestion 10

def flip(s, a, b):
    return s[b:] + s[a:b] + s[:a]

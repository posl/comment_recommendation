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
    #print(N, S, Q, T, A, B)
    S1 = S[:N]
    S2 = S[N:]
    #print(S1, S2)
    for i in range(Q):
        if T[i] == 1:
            A[i] -= 1
            B[i] -= 1
            if A[i] < N:
                if B[i] < N:
                    S1 = S1[:A[i]] + S1[B[i]] + S1[A[i]+1:B[i]] + S1[A[i]] + S1[B[i]+1:]
                else:
                    S1 = S1[:A[i]] + S2[B[i]-N] + S1[A[i]+1:]
                    S2 = S2[:B[i]-N] + S1[A[i]] + S2[B[i]-N+1:]
            else:
                if B[i] < N:
                    S2 = S2[:A[i]-N] + S1[B[i]] + S2[A[i]-N+1:]
                    S1 = S1[:B[i]] + S2[A[i]-N] + S1[B[i]+1:]
                else:
                    S2 = S2[:A[i]-N] + S2[B[i]-N] + S2[A[i]-N+1:B[i]-N] + S2[A[i]-N] + S2[B[i]-N+1:]
        else:
            S1, S2 = S2, S1
        #print(S1, S2)
    print(S1 + S2)

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
    swich = 0
    for i in range(Q):
        if T[i] == 1:
            if swich == 0:
                if A[i] <= N and B[i] <= N:
                    S = S[:A[i]-1] + S[B[i]-1] + S[A[i]:B[i]-1] + S[A[i]-1] + S[B[i]:]
                elif A[i] <= N and B[i] > N:
                    S = S[:A[i]-1] + S[B[i]-1] + S[A[i]:N] + S[A[i]-1] + S[N:B[i]-1] + S[N+A[i]-1] + S[B[i]:]
                elif A[i] > N and B[i] > N:
                    S = S[:A[i]-1] + S[B[i]-1] + S[A[i]:B[i]-1] + S[A[i]-1] + S[B[i]:]
            else:
                if A[i] <= N and B[i] <= N:
                    S = S[:N+A[i]-1] + S[N+B[i]-1] + S[N+A[i]:N+B[i]-1] + S[N+A[i]-1] + S[N+B[i]:]
                elif A[i] <= N and B[i] > N:
                    S = S[:N+A[i]-1] + S[N+B[i]-1] + S[N+A[i]:N] + S[N+A[i]-1] + S[N:N+B[i]-1] + S[A[i]-1] + S[N+B[i]:]
                elif A[i] > N and B[i] > N:
                    S = S[:N+A[i]-1] + S[N+B[i]-1] + S[N+A[i]:N+B[i]-1] + S[N+A[i]-1] + S[N+B[i]:]
        else:
            if swich == 0:
                swich = 1
            else:
                swich = 0
    if swich

=======
Suggestion 3

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
    
    #N = 2
    #S = "FLIP"
    #Q = 6
    #T = [1, 2, 1, 1, 2, 1]
    #A = [1, 0, 1, 2, 0, 1]
    #B = [3, 0, 2, 3, 0, 4]
    
    #N = 2
    #S = "FLIP"
    #Q = 2
    #T = [2, 1]
    #A = [0, 1]
    #B = [0, 4]
    
    #N = 2
    #S = "FLIP"
    #Q = 2
    #T = [1, 2]
    #A = [1, 0]
    #B = [4, 0]
    
    #N = 2
    #S = "FLIP"
    #Q = 2
    #T = [1, 1]
    #A = [1, 2]
    #B = [4, 3]
    
    #N = 2
    #S = "FLIP"
    #Q = 2
    #T = [1, 1]
    #A = [1, 1]
    #B = [4, 4]
    
    #N = 2
    #S = "FLIP"
    #Q = 2
    #T = [1, 1]
    #A = [1, 1]
    #B = [4, 4]
    
    #N = 2
    #S = "FLIP"
    #Q = 2
    #T = [1, 1]
    #A = [1, 1]
    #B = [4, 4]
    
    #N = 2
    #

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
    S = list(S)
    #print(S)
    #print("".join(S))
    swap = 0
    for i in range(Q):
        if T[i] == 1:
            if swap == 0:
                S[A[i]-1], S[B[i]-1] = S[B[i]-1], S[A[i]-1]
            else:
                if A[i] <= N:
                    if B[i] <= N:
                        S[A[i]-1+N], S[B[i]-1+N] = S[B[i]-1+N], S[A[i]-1+N]
                    else:
                        S[A[i]-1+N], S[B[i]-1-N] = S[B[i]-1-N], S[A[i]-1+N]
                else:
                    if B[i] <= N:
                        S[A[i]-1-N], S[B[i]-1+N] = S[B[i]-1+N], S[A[i]-1-N]
                    else:
                        S[A[i]-1-N], S[B[i]-1-N] = S[B[i]-1-N], S[A[i]-1-N]
        else:
            swap = 1 - swap
        #print("".join(S))
    if swap == 1:
        S = S[N:] + S[:N]
    print("".join(S))

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
    #print(N, S, Q, T, A, B)

    # 0: 1st half, 1: 2nd half
    half = 0
    for i in range(Q):
        if T[i] == 1:
            if half == 0:
                if A[i] <= N and B[i] <= N:
                    A[i] -= 1
                    B[i] -= 1
                    S = S[:A[i]] + S[B[i]] + S[A[i]+1:B[i]] + S[A[i]] + S[B[i]+1:]
                elif A[i] <= N and B[i] > N:
                    A[i] -= 1
                    B[i] -= N + 1
                    S = S[:A[i]] + S[B[i]] + S[A[i]+1:B[i]] + S[A[i]] + S[B[i]+1:]
                elif A[i] > N and B[i] <= N:
                    A[i] -= N + 1
                    B[i] -= 1
                    S = S[:A[i]] + S[B[i]] + S[A[i]+1:B[i]] + S[A[i]] + S[B[i]+1:]
                else:
                    A[i] -= N + 1
                    B[i] -= N + 1
                    S = S[:A[i]] + S[B[i]] + S[A[i]+1:B[i]] + S[A[i]] + S[B[i]+1:]
            else:
                if A[i] <= N and B[i] <= N:
                    A[i] -= 1
                    B[i] -= 1
                    S = S[:A[i]] + S[B[i]] + S[A[i]+1:B[i]] + S[A[i]] + S[B[i]+1:]
                elif A[i] <= N and B[i] > N:
                    A[i] -= 1
                    B[i] -= N + 1
                    S = S[:A[i]] + S[B[i]] + S[A[i]+1

=======
Suggestion 6

def main():
    N = int(input())
    S = input()
    Q = int(input())
    for i in range(Q):
        T, A, B = map(int, input().split())
        if T == 1:
            S = S[:A-1] + S[B-1] + S[A:B-1] + S[A-1] + S[B:]
        else:
            S = S[N:] + S[:N]
    print(S)

=======
Suggestion 7

def main():
    #input
    N = int(input())
    S = input()
    Q = int(input())
    T = [0]*Q
    A = [0]*Q
    B = [0]*Q
    for i in range(Q):
        T[i],A[i],B[i] = map(int,input().split())
    
    #processing
    s1 = S[:N]
    s2 = S[N:]
    for i in range(Q):
        if T[i] == 1:
            if A[i] <= N:
                if B[i] <= N:
                    s1 = s1[:A[i]-1] + s1[B[i]-1] + s1[A[i]:B[i]-1] + s1[A[i]-1] + s1[B[i]:]
                else:
                    s1 = s1[:A[i]-1] + s2[B[i]-N-1] + s1[A[i]:B[i]-N-1] + s1[A[i]-1] + s1[B[i]-N:]
                    s2 = s2[:B[i]-N-1] + s1[A[i]-1] + s2[A[i]:B[i]-N-1] + s2[B[i]-N-1] + s2[B[i]-N:]
            else:
                if B[i] <= N:
                    s2 = s2[:A[i]-N-1] + s1[B[i]-1] + s2[A[i]-N:B[i]-1] + s2[A[i]-N-1] + s2[B[i]:]
                    s1 = s1[:B[i]-1] + s2[A[i]-N-1] + s1[A[i]:B[i]-1] + s1[B[i]-1] + s1[B[i]:]
                else:
                    s2 = s2[:A[i]-N-1] + s2[B[i]-N-1] + s2[A[i]-N:B[i]-N-1] + s2[A[i]-N-1] + s2[B[i]-N:]
        else:
            s1,s2 = s2,s1
    
    #output
    print(s1+s2)

=======
Suggestion 8

def main():
    N = int(input())
    S = input()
    Q = int(input())
    queries = [list(map(int, input().split())) for _ in range(Q)]
    s = S[:N]
    t = S[N:]
    flip = False
    for q in queries:
        if q[0] == 1:
            if q[1] <= N and q[2] <= N:
                if flip:
                    q[1] += N
                    q[2] += N
                s = swap(s, q[1]-1, q[2]-1)
            elif q[1] > N and q[2] > N:
                if not flip:
                    q[1] -= N
                    q[2] -= N
                t = swap(t, q[1]-1, q[2]-1)
            else:
                if not flip:
                    q[1] -= N
                    q[2] += N
                else:
                    q[1] += N
                    q[2] -= N
                s = swap(s, q[1]-1, q[2]-1)
        else:
            flip = not flip
    if flip:
        print(t+s)
    else:
        print(s+t)

=======
Suggestion 9

def flip(s, a, b):
    return s[:a] + s[b] + s[a+1:b] + s[a] + s[b+1:]

=======
Suggestion 10

def readInts():
    return list(map(int, input().split()))

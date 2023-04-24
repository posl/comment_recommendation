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
    S = list(S)
    #print(S)
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
            A[i] -= 1
            B[i] -= 1
            S[A[i]], S[B[i]] = S[B[i]], S[A[i]]
        else:
            flip = not flip
    if flip:
        S = S[N:] + S[:N]
    print(''.join(S))

=======
Suggestion 2

def main():
    N = int(input())
    S = input()
    Q = int(input())
    T = [0]*Q
    A = [0]*Q
    B = [0]*Q
    for i in range(Q):
        T[i], A[i], B[i] = map(int, input().split())
    S = list(S)
    swap = False
    for i in range(Q):
        if T[i] == 1:
            if swap:
                A[i] = (A[i] - 1 + N) % (2*N) + 1
                B[i] = (B[i] - 1 + N) % (2*N) + 1
            A[i] -= 1
            B[i] -= 1
            S[A[i]], S[B[i]] = S[B[i]], S[A[i]]
        else:
            swap = not swap
    if swap:
        S = S[N:] + S[:N]
    print(''.join(S))

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
    #print(N, S, Q, T, A, B)
    ans = S
    for i in range(Q):
        if T[i] == 1:
            ans = ans[:A[i]-1] + ans[B[i]-1] + ans[A[i]:B[i]-1] + ans[A[i]-1] + ans[B[i]:]
        else:
            ans = ans[N:] + ans[:N]
    print(ans)

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
    print(solve(N, S, Q, T, A, B))

=======
Suggestion 5

def main():
    n = int(input())
    s = input()
    q = int(input())
    t = [0] * q
    a = [0] * q
    b = [0] * q
    for i in range(q):
        t[i], a[i], b[i] = map(int, input().split())
    
    l = [0] * n
    r = [0] * n
    for i in range(n):
        l[i] = i
        r[i] = i + n
    
    for i in range(q):
        if t[i] == 1:
            a[i] -= 1
            b[i] -= 1
            if a[i] < n and b[i] < n:
                l[a[i]], l[b[i]] = l[b[i]], l[a[i]]
            elif a[i] < n and b[i] >= n:
                l[a[i]], r[b[i] - n] = r[b[i] - n], l[a[i]]
            elif a[i] >= n and b[i] < n:
                r[a[i] - n], l[b[i]] = l[b[i]], r[a[i] - n]
            else:
                r[a[i] - n], r[b[i] - n] = r[b[i] - n], r[a[i] - n]
        else:
            l, r = r, l
    
    ans = ""
    for i in range(n):
        ans += s[l[i]]
    for i in range(n):
        ans += s[r[i]]
    print(ans)

=======
Suggestion 6

def main():
    N = int(input())
    S = input()
    Q = int(input())
    T = []
    A = []
    B = []
    for _ in range(Q):
        t, a, b = map(int, input().split())
        T.append(t)
        A.append(a)
        B.append(b)
    
    S1 = S[:N]
    S2 = S[N:]
    for t, a, b in zip(T, A, B):
        if t == 1:
            if a <= N:
                if b <= N:
                    S1 = S1[:a-1] + S1[b-1] + S1[a:b-1] + S1[a-1] + S1[b:]
                else:
                    S1 = S1[:a-1] + S2[b-N-1] + S1[a:b-N-1] + S1[a-1] + S1[b-N:]
                    S2 = S2[:b-N-1] + S1[a-1] + S2[a:b-N-1] + S2[b-N:]
            else:
                if b <= N:
                    S1 = S1[:b-1] + S2[a-N-1] + S1[b:a-N-1] + S1[b-1] + S1[a-N:]
                    S2 = S2[:a-N-1] + S1[b-1] + S2[b:a-N-1] + S2[a-N:]
                else:
                    S2 = S2[:a-N-1] + S2[b-N-1] + S2[a-N:b-N-1] + S2[a-N-1] + S2[b-N:]
        else:
            S1, S2 = S2, S1
    
    print(S1 + S2)

=======
Suggestion 7

def main():
    n = int(input())
    s = list(input())
    q = int(input())
    for i in range(q):
        t,a,b = map(int,input().split())
        if t == 1:
            s[a-1],s[b-1] = s[b-1],s[a-1]
        else:
            if n == 1:
                s[0],s[1] = s[1],s[0]
            else:
                s[0],s[1] = s[1],s[0]
                s[2],s[3] = s[3],s[2]
    print(''.join(s))

=======
Suggestion 8

def get_input():
    N = int(input())
    S = input()
    Q = int(input())
    T = [0] * Q
    A = [0] * Q
    B = [0] * Q
    for i in range(Q):
        T[i], A[i], B[i] = map(int, input().split())
    return N, S, Q, T, A, B

=======
Suggestion 9

def main():
    N = int(input())
    S = input()
    Q = int(input())
    T_A_B = [list(map(int,input().split())) for _ in range(Q)]
    S = list(S)
    S1 = S[:N]
    S2 = S[N:]
    C = 0 # 1: S1,S2の入れ替え
    for t,a,b in T_A_B:
        if t == 1:
            if C == 0:
                S1[a-1],S1[b-1] = S1[b-1],S1[a-1]
            else:
                S2[a-1],S2[b-1] = S2[b-1],S2[a-1]
        else:
            C = 1-C
    if C == 0:
        print("".join(S1+S2))
    else:
        print("".join(S2+S1))

=======
Suggestion 10

def main():
    N = int(input())
    S = input()
    Q = int(input())
    #print(N, S, Q)
    #print()
    T = []
    A = []
    B = []
    for i in range(Q):
        t, a, b = map(int, input().split())
        T.append(t)
        A.append(a)
        B.append(b)
    #print(T, A, B)
    #print()
    #print

Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    N = int(input())
    S = list(input())
    Q = int(input())
    for _ in range(Q):
        T, A, B = map(int, input().split())
        if T == 1:
            S[A - 1], S[B - 1] = S[B - 1], S[A - 1]
        else:
            S = S[N:] + S[:N]
    print("".join(S))

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
    
    S1 = S[:N]
    S2 = S[N:]
    
    for i in range(Q):
        if T[i] == 1:
            if A[i] <= N:
                if B[i] <= N:
                    S1 = S1[:A[i]-1] + S1[B[i]-1] + S1[A[i]:B[i]-1] + S1[A[i]-1] + S1[B[i]:]
                else:
                    S1 = S1[:A[i]-1] + S2[B[i]-N-1] + S1[A[i]:B[i]-N-1] + S1[A[i]-1] + S1[B[i]-N:]
                    S2 = S2[:B[i]-N-1] + S1[A[i]-1] + S2[A[i]:B[i]-N-1] + S2[B[i]-N-1] + S2[B[i]-N:]
            else:
                if B[i] <= N:
                    S2 = S2[:A[i]-N-1] + S1[B[i]-1] + S2[A[i]-N:B[i]-1] + S2[A[i]-N-1] + S2[B[i]:]
                    S1 = S1[:B[i]-1] + S2[A[i]-N-1] + S1[A[i]:B[i]-1] + S1[B[i]-1] + S1[B[i]:]
                else:
                    S2 = S2[:A[i]-N-1] + S2[B[i]-N-1] + S2[A[i]-N:B[i]-N-1] + S2[A[i]-N-1] + S2[B[i]-N:]
        else:
            S1, S2 = S2, S1
    
    print(S1 + S2)

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
    ans = S
    rev = False
    for i in range(Q):
        if T[i] == 1:
            if rev:
                A[i] = (A[i] + N - 1) % (2 * N) + 1
                B[i] = (B[i] + N - 1) % (2 * N) + 1
            A[i] -= 1
            B[i] -= 1
            ans = ans[:A[i]] + ans[B[i]] + ans[A[i] + 1:B[i]] + ans[A[i]] + ans[B[i] + 1:]
        else:
            rev = not rev
    if rev:
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
    
    for i in range(Q):
        if T[i] == 1:
            S = S[:A[i]-1] + S[B[i]-1] + S[A[i]:B[i]-1] + S[A[i]-1] + S[B[i]:]
        else:
            S = S[N:] + S[:N]
    
    print(S)

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
            S = S[:A[i]-1] + S[B[i]-1] + S[A[i]:B[i]-1] + S[A[i]-1] + S[B[i]:]
        elif T[i] == 2:
            S = S[N:] + S[:N]
        else:
            print('error')
            break
    print(S)

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
    S = list(S)
    for i in range(Q):
        if T[i] == 1:
            S[A[i]-1], S[B[i]-1] = S[B[i]-1], S[A[i]-1]
        else:
            S = S[N:] + S[:N]
    print("".join(S))

=======
Suggestion 7

def main():
    n = int(input())
    s = input()
    q = int(input())
    for i in range(q):
        t, a, b = map(int, input().split())
        if t == 1:
            a -= 1
            b -= 1
            s = s[:a] + s[b] + s[a+1:b] + s[a] + s[b+1:]
        else:
            s = s[n:] + s[:n]
    print(s)

=======
Suggestion 8

def main():
    n = int(input())
    s = input()
    q = int(input())
    queries = [list(map(int, input().split())) for _ in range(q)]
    for query in queries:
        if query[0] == 1:
            s = s[:query[1]-1] + s[query[2]-1] + s[query[1]:query[2]-1] + s[query[1]-1] + s[query[2]:]
        elif query[0] == 2:
            s = s[n:] + s[:n]
    print(s)

=======
Suggestion 9

def main():
    N = int(input())
    S = input()
    Q = int(input())
    # 1, 2, 3, 4, 5, 6, 7, 8
    # F, L, I, P, F, L, I, P
    # 1, 2, 3, 4, 5, 6, 7, 8
    # F, L, I, P, F, L, I, P
    # 1, 2, 3, 4, 5, 6, 7, 8
    # F, L, I, P, F, L, I, P
    # 1, 2, 3, 4, 5, 6, 7, 8
    # F, L, I, P, F, L, I, P
    # 1, 2, 3, 4, 5, 6, 7, 8
    # F, L, I, P, F, L, I, P
    # 1, 2, 3, 4, 5, 6, 7, 8
    # F, L, I, P, F, L, I, P
    # 1, 2, 3, 4, 5, 6, 7, 8
    # F, L, I, P, F, L, I, P
    # 1, 2, 3, 4, 5, 6, 7, 8
    # F, L, I, P, F, L, I, P
    # 1, 2, 3, 4, 5, 6, 7, 8
    # F, L, I, P, F, L, I, P
    # 1, 2, 3, 4, 5, 6, 7, 8
    # F, L, I, P, F, L, I, P
    # 1, 2, 3, 4, 5, 6, 7, 8
    # F, L, I, P, F, L, I

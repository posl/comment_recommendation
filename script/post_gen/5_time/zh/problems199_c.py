Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N = int(input())
    S = list(input())
    Q = int(input())
    T = [0] * Q
    A = [0] * Q
    B = [0] * Q
    for i in range(Q):
        T[i], A[i], B[i] = map(int, input().split())
    #print("N=", N)
    #print("S=", S)
    #print("Q=", Q)
    #print("T=", T)
    #print("A=", A)
    #print("B=", B)

    #print("".join(S))
    for i in range(Q):
        if T[i] == 1:
            S[A[i]-1], S[B[i]-1] = S[B[i]-1], S[A[i]-1]
        elif T[i] == 2:
            S[0:N], S[N:2*N] = S[N:2*N], S[0:N]
        #print("".join(S))
    print("".join(S))

=======
Suggestion 2

def exchange(s, a, b):
    if a < b:
        return s[:a] + s[b] + s[a+1:b] + s[a] + s[b+1:]
    else:
        return s[:b] + s[a] + s[b+1:a] + s[b] + s[a+1:]

=======
Suggestion 3

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
            if a[i] <= n:
                a[i] = a[i] + n
            else:
                a[i] = a[i] - n
            if b[i] <= n:
                b[i] = b[i] + n
            else:
                b[i] = b[i] - n
            s = s[:a[i]-1] + s[b[i]-1] + s[a[i]:b[i]-1] + s[a[i]-1] + s[b[i]:]
        else:
            s = s[n:] + s[:n]
    print(s)

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
        t_a_b = input()
        t_a_b = t_a_b.split()
        t.append(int(t_a_b[0]))
        a.append(int(t_a_b[1]))
        b.append(int(t_a_b[2]))
    for i in range(q):
        if t[i] == 1:
            s = s[:a[i]-1] + s[b[i]-1] + s[a[i]:b[i]-1] + s[a[i]-1] + s[b[i]:]
        else:
            s = s[n:] + s[:n]
    print(s)

=======
Suggestion 5

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
    rev = 0
    for i in range(Q-1, -1, -1):
        if T[i] == 2:
            rev = 1 - rev
        else:
            if rev == 1:
                if A[i] <= N:
                    A[i] += N
                else:
                    A[i] -= N
                if B[i] <= N:
                    B[i] += N
                else:
                    B[i] -= N
            S = S[:A[i]-1] + S[B[i]-1] + S[A[i]:B[i]-1] + S[A[i]-1] + S[B[i]:]
    if rev == 1:
        S = S[N:] + S[:N]
    print(S)

=======
Suggestion 6

def main():
    n = int(input())
    s = input()
    q = int(input())

    is_reverse = False
    left = s[:n]
    right = s[n:]

    for i in range(q):
        t, a, b = map(int, input().split())
        a -= 1
        b -= 1

        if t == 1:
            if is_reverse:
                if a >= n:
                    a -= n
                else:
                    a += n
                if b >= n:
                    b -= n
                else:
                    b += n
            left = left[:a] + right[b] + left[a+1:]
            right = right[:b] + left[a] + right[b+1:]
        else:
            is_reverse = not is_reverse

    if is_reverse:
        left, right = right, left

    print(left + right)

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
        elif T[i] == 2:
            S = S[N:] + S[:N]
    print(S)

=======
Suggestion 8

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
    rev = False
    for i in range(Q):
        if T[i] == 1:
            if rev:
                if A[i] <= N:
                    A[i] += N
                else:
                    A[i] -= N
                if B[i] <= N:
                    B[i] += N
                else:
                    B[i] -= N
            S = S[:A[i] - 1] + S[B[i] - 1] + S[A[i]:B[i] - 1] + S[A[i] - 1] + S[B[i]:]
        else:
            rev = not rev
    if rev:
        S = S[N:] + S[:N]
    print(S)

=======
Suggestion 9

def swap(s, i, j):
    if i > j:
        i, j = j, i
    return s[:i] + s[j] + s[i+1:j] + s[i] + s[j+1:]

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
    for i in range(q):
        if t[i] == 1:
            s = s[:a[i]-1] + s[b[i]-1] + s[a[i]:b[i]-1] + s[a[i]-1] + s[b[i]:]
        else:
            s = s[n:] + s[:n]
    print(s)

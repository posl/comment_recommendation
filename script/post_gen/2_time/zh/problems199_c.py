Synthesizing 10/10 solutions

=======
Suggestion 1

def swap(s, a, b):
    if a > b:
        a, b = b, a
    return s[:a-1] + s[b-1] + s[a:b-1] + s[a-1] + s[b:]

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
    flag = False
    for i in range(q-1, -1, -1):
        if t[i] == 1:
            if flag:
                if a[i] <= n:
                    a[i] += n
                else:
                    a[i] -= n
                if b[i] <= n:
                    b[i] += n
                else:
                    b[i] -= n
            s = s[0:a[i]-1] + s[b[i]-1] + s[a[i]:b[i]-1] + s[a[i]-1] + s[b[i]:]
        else:
            flag = not flag
    if flag:
        s = s[n:] + s[:n]
    print(s)

=======
Suggestion 3

def solve(n, s, q, query):
    #print("n,s,q,query=",n,s,q,query)
    #print("s[0:n]=",s[0:n])
    #print("s[n:2*n]=",s[n:2*n])
    #print("s=",s)
    for i in range(q):
        #print("i=",i)
        #print("query[i][0]=",query[i][0])
        #print("query[i][1]=",query[i][1])
        #print("query[i][2]=",query[i][2])
        if query[i][0] == 1:
            #print("s[query[i][1]-1]=",s[query[i][1]-1])
            #print("s[query[i][2]-1]=",s[query[i][2]-1])
            #print("s[query[i][1]-1],s[query[i][2]-1]=",s[query[i][1]-1],s[query[i][2]-1])
            s[query[i][1]-1], s[query[i][2]-1] = s[query[i][2]-1], s[query[i][1]-1]
            #print("s[query[i][1]-1],s[query[i][2]-1]=",s[query[i][1]-1],s[query[i][2]-1])
        elif query[i][0] == 2:
            #print("s[0:n]=",s[0:n])
            #print("s[n:2*n]=",s[n:2*n])
            s[0:n], s[n:2*n] = s[n:2*n], s[0:n]
            #print("s[0:n]=",s[0:n])
            #print("s[n:2*n]=",s[n:2*n])
    return s

=======
Suggestion 4

def solve():
    n = int(input())
    s = input()
    q = int(input())
    s1 = s[:n]
    s2 = s[n:]
    for _ in range(q):
        t, a, b = map(int, input().split())
        if t == 1:
            if a <= n:
                a -= 1
                b -= 1
                s1[a], s1[b] = s1[b], s1[a]
            else:
                a -= n + 1
                b -= n + 1
                s2[a], s2[b] = s2[b], s2[a]
        else:
            s1, s2 = s2, s1
    print(''.join(s1) + ''.join(s2))

=======
Suggestion 5

def main():

    N = int(input())
    S = input()
    Q = int(input())

    #print(N)
    #print(S)
    #print(Q)

    #print("S[:N] = ", S[:N])
    #print("S[N:] = ", S[N:])

    for i in range(Q):
        T, A, B = map(int, input().split())
        #print("T = ", T, "A = ", A, "B = ", B)
        if T == 1:
            S = S[:A-1] + S[B-1] + S[A:B-1] + S[A-1] + S[B:]
        else:
            S = S[N:] + S[:N]
        #print("S = ", S)
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

=======
Suggestion 7

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
    reverse = False
    for i in range(Q):
        if T[i] == 1:
            if reverse:
                A[i] += N
                B[i] += N
                if A[i] > 2 * N:
                    A[i] -= 2 * N
                if B[i] > 2 * N:
                    B[i] -= 2 * N
            S = S[:A[i]-1] + S[B[i]-1] + S[A[i]:B[i]-1] + S[A[i]-1] + S[B[i]:]
        else:
            reverse = not reverse
    if reverse:
        S = S[N:] + S[:N]
    print(S)

solve()

=======
Suggestion 8

def main():
    n = int(input())
    s = input()
    q = int(input())
    s1 = s[:n]
    s2 = s[n:]
    for i in range(q):
        t, a, b = map(int, input().split())
        if t == 1:
            if a <= n:
                a -= 1
                if b <= n:
                    b -= 1
                    s1 = s1[:a] + s1[b] + s1[a+1:b] + s1[a] + s1[b+1:]
                else:
                    b -= n+1
                    s1 = s1[:a] + s2[b] + s1[a+1:]
                    s2 = s2[:b] + s1[a] + s2[b+1:]
            else:
                a -= n+1
                if b <= n:
                    b -= 1
                    s2 = s2[:a] + s1[b] + s2[a+1:]
                    s1 = s1[:b] + s2[a] + s1[b+1:]
                else:
                    b -= n+1
                    s2 = s2[:a] + s2[b] + s2[a+1:b] + s2[a] + s2[b+1:]
        else:
            s1, s2 = s2, s1
    print(s1 + s2)

main()

=======
Suggestion 9

def solve():
    n = int(input())
    s = input()
    q = int(input())
    s = list(s)
    rev = False
    for _ in range(q):
        t, a, b = map(int, input().split())
        if t == 1:
            if rev:
                a = a + n if a <= n else a - n
                b = b + n if b <= n else b - n
            s[a-1], s[b-1] = s[b-1], s[a-1]
        else:
            rev = not rev
    if rev:
        s = s[n:] + s[:n]
    print(''.join(s))

=======
Suggestion 10

def process(S, T, A, B):
    if T == 1:
        # S[A-1], S[B-1] = S[B-1], S[A-1]  # 为什么不行？
        S[A-1], S[B-1] = S[B-1], S[A-1]
    elif T == 2:
        S[:len(S)//2], S[len(S)//2:] = S[len(S)//2:], S[:len(S)//2]
    return S

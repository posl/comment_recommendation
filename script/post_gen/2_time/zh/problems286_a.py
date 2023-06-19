Synthesizing 10/10 solutions

=======
Suggestion 1

def swap_list(list, p, q, r, s):
    tmp = list[p-1:q]
    list[p-1:q] = list[r-1:s]
    list[r-1:s] = tmp
    return list

=======
Suggestion 2

def swap(A, P, Q, R, S):
    B = A.copy()
    for i in range(P-1, Q):
        B[i] = A[R+i-Q]
    for i in range(R-1, S):
        B[i] = A[P+i-R]
    return B

=======
Suggestion 3

def swap(a, b, c, d, e):
    for i in range(b, c):
        a[i], a[i+d-b] = a[i+d-b], a[i]
    return a

n, p, q, r, s = map(int, input().split())
a = list(map(int, input().split()))
swap(a, p-1, q, r, s)
print(*a)

=======
Suggestion 4

def swap(a, b):
    temp = a
    a = b
    b = temp
    return a, b

=======
Suggestion 5

def swap(A, P, Q, R, S):
    B = A.copy()
    for i in range(P-1, Q):
        B[i] = A[i+R-Q]
    for i in range(R-1, S):
        B[i] = A[i+P-R]
    return B

=======
Suggestion 6

def swap(a, p, q, r, s):
    b = a.copy()
    for i in range(q-p+1):
        b[p+i-1] = a[s+i-1]
    for i in range(s-r+1):
        b[r+i-1] = a[q+i-1]
    return b

=======
Suggestion 7

def main():
    N, P, Q, R, S = map(int, input().split())
    A = list(map(int, input().split()))
    B = A.copy()
    for i in range(P-1, Q):
        B[i] = A[i+R-Q]
    for i in range(R-1, S):
        B[i] = A[i+P-R]
    for i in range(N):
        print(B[i], end=' ')
    print()

=======
Suggestion 8

def main():
    N,P,Q,R,S = map(int, input().split())
    A = list(map(int, input().split()))
    B = []
    for i in range(N):
        if i >= P-1 and i <= Q-1:
            B.append(A[i+R-Q])
        elif i >= R-1 and i <= S-1:
            B.append(A[i+P-R])
        else:
            B.append(A[i])
    for i in range(N):
        print(B[i], end = ' ')

=======
Suggestion 9

def problems286_a():
    n, p, q, r, s = map(int, input().split())
    a = list(map(int, input().split()))
    b = [0] * n
    for i in range(n):
        if i < p - 1:
            b[i + s - q] = a[i]
        elif i < r - 1:
            b[i - p + q] = a[i]
        else:
            b[i + s - r] = a[i]
    print(*b)

=======
Suggestion 10

def main():
    N,P,Q,R,S = map(int,input().split())
    A = list(map(int,input().split()))
    B = A[0:P-1] + A[R-1:S] + A[Q-1:R-1] + A[P-1:Q-1] + A[S:]
    for i in range(N):
        if i == N-1:
            print(B[i])
        else:
            print(B[i],end=' ')

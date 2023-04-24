Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N, P, Q, R, S = map(int, input().split())
    A = list(map(int, input().split()))
    B = A[:P-1] + A[Q:R-1] + A[S:]
    print(' '.join(map(str, B)))

=======
Suggestion 2

def main():
    N, P, Q, R, S = map(int, input().split())
    A = list(map(int, input().split()))
    B = A[:P-1] + A[Q:R-1] + A[S:]
    print(*B)

=======
Suggestion 3

def main():
    N, P, Q, R, S = map(int, input().split())
    A = list(map(int, input().split()))
    B = A[P-1:Q] + A[R-1:S]
    print(*B)

=======
Suggestion 4

def main():
    n, p, q, r, s = map(int, input().split())
    a = list(map(int, input().split()))
    print(*a[:p-1], *a[q:r-1:-1], *a[s-1:p-1:-1], *a[r-1:], sep=' ')

=======
Suggestion 5

def main():
    n, p, q, r, s = map(int, input().split())
    a = list(map(int, input().split()))
    b = a[:]
    b[p - 1:q] = a[q - 1:r - 1: -1]
    b[r - 1:s] = a[s - 1:p - 1: -1]
    print(*b)

=======
Suggestion 6

def main():
    N,P,Q,R,S = map(int, input().split())
    A = list(map(int, input().split()))
    B = A[0:P-1] + A[Q:R-1] + A[S-1:N]
    print(*B)

=======
Suggestion 7

def swap(a, p, q, r, s):
    b = []
    for i in range(p-1):
        b.append(a[i])
    for i in range(r-1, s):
        b.append(a[i])
    for i in range(q, r-1):
        b.append(a[i])
    for i in range(s, len(a)):
        b.append(a[i])
    return b

=======
Suggestion 8

def swap(a, p, q, r, s):
    b = a[0:p-1]
    b.extend(a[r-1:s])
    b.extend(a[q:r-1])
    b.extend(a[p-1:q])
    b.extend(a[s:])
    return b

=======
Suggestion 9

def main():
    #input
    N,P,Q,R,S=map(int,input().split())
    A=list(map(int,input().split()))
    #output
    print(' '.join(map(str,A[P-1:Q]+A[R-1:S])))

=======
Suggestion 10

def swap(a, b, c, d):
    #a = list, b = p, c = q, d = r, e = s
    e = d
    temp = a[b-1:c]
    a[b-1:c] = a[d-1:e]
    a[d-1:e] = temp
    return a

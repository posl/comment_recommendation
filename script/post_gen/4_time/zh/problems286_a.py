Synthesizing 10/10 solutions

=======
Suggestion 1

def swap(arr, p, q, r, s):
    arr[p-1:q], arr[r-1:s] = arr[r-1:s], arr[p-1:q]
    return arr

=======
Suggestion 2

def swap(a, p, q, r, s):
    b = a[p-1:q] + a[r-1:s] + a[q:r-1] + a[s:]
    return b

=======
Suggestion 3

def main():
    N,P,Q,R,S = map(int,input().split())
    A = list(map(int,input().split()))
    B = []
    for i in range(N):
        B.append(A[i])
    for i in range(N):
        if i < P-1 or i > S-1:
            print(B[i],end=' ')
        elif i >= P-1 and i < Q-1:
            print(B[i+R-Q],end=' ')
        elif i >= Q-1 and i < R-1:
            print(B[i+P-Q],end=' ')
        else:
            print(B[i+S-R],end=' ')

=======
Suggestion 4

def swap(arr, p, q, r, s):
    arr1 = arr[:p]
    arr2 = arr[p:q]
    arr3 = arr[q:r]
    arr4 = arr[r:s]
    arr5 = arr[s:]
    arr = arr1 + arr4 + arr3 + arr2 + arr5
    return arr

=======
Suggestion 5

def main():
    n,p,q,r,s = map(int, input().split())
    a = list(map(int, input().split()))
    b = []
    for i in range(n):
        if i >= p-1 and i <= q-1:
            b.append(a[i+r-q])
        elif i >= r-1 and i <= s-1:
            b.append(a[i-q+p])
        else:
            b.append(a[i])
    print(' '.join(map(str, b)))

=======
Suggestion 6

def swap(a, b):
    return b, a

=======
Suggestion 7

def swap(A, P, Q, R, S):
    B = A[:P-1] + A[R-1:S] + A[Q-1:R-1] + A[P-1:Q-1] + A[S:]
    return B

N, P, Q, R, S = map(int, input().split())
A = list(map(int, input().split()))
B = swap(A, P, Q, R, S)
print(" ".join(map(str, B)))

=======
Suggestion 8

def swap(A, P, Q, R, S):
    B = A.copy()
    for i in range(P-1, Q):
        B[i] = A[i+R-Q]
    for i in range(R-1, S):
        B[i] = A[i+P-R]
    return B

=======
Suggestion 9

def main():
    N, P, Q, R, S = map(int, input().split())
    A = list(map(int, input().split()))
    B = A[P - 1:Q] + A[R - 1:S]
    A[P - 1:Q] = B[R - 1:S]
    A[R - 1:S] = B[:Q - P]
    print(*A)

=======
Suggestion 10

def main():
    N, P, Q, R, S = map(int, input().split())
    A = list(map(int, input().split()))
    B = []
    B.extend(A[P-1:Q])
    B.extend(A[R-1:S])
    B.extend(A[Q:R-1])
    B.extend(A[S:])
    print(' '.join(map(str, B)))

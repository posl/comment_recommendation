Synthesizing 10/10 solutions

=======
Suggestion 1

def solve():
    N, P, Q, R, S = list(map(int, input().split()))
    A = list(map(int, input().split()))
    B = A[:P-1] + A[R-1:S] + A[Q-1:R-1] + A[S:]
    print(" ".join(map(str, B)))

=======
Suggestion 2

def swap(a, p, q, r, s):
    b = a[:p]
    b.extend(a[r:s+1])
    b.extend(a[q+1:r])
    b.extend(a[p:q+1])
    b.extend(a[s+1:])
    return b

=======
Suggestion 3

def swap(arr, p, q, r, s):
    arr[p-1:q], arr[r-1:s] = arr[r-1:s], arr[p-1:q]
    return arr

=======
Suggestion 4

def swap(a, p, q, r, s):
    b = a[0:p-1]
    b.extend(a[r-1:s])
    b.extend(a[q:s])
    b.extend(a[p-1:r-1])
    b.extend(a[s:])
    return b

=======
Suggestion 5

def swap_array(a, p, q, r, s):
    b = a[:p]
    b.extend(a[r:s+1])
    b.extend(a[q+1:r])
    b.extend(a[p:q+1])
    b.extend(a[s+1:])
    return b

=======
Suggestion 6

def swap(a, p, q, r, s):
    b = a.copy()
    for i in range(p-1, q):
        b[i] = a[r-1+i-q]
    for i in range(r-1, s):
        b[i] = a[p-1+i-r]
    return b

=======
Suggestion 7

def swap(arr, p, q, r, s):
    b = arr.copy()
    for i in range(p-1, q):
        b[i] = arr[i+r-q]
    for i in range(r-1, s):
        b[i] = arr[i-q+p]
    return b

=======
Suggestion 8

def myCode():
    n, p, q, r, s = map(int, input().split())
    a = list(map(int, input().split()))

    for i in range(n):
        if i+1 == p or i+1 == q or i+1 == r or i+1 == s:
            print(a[r-1], end=' ')
        elif i+1 == r or i+1 == s:
            print(a[p-1], end=' ')
        else:
            print(a[i], end=' ')

=======
Suggestion 9

def swap(a, b):
    temp = a
    a = b
    b = temp
    return a, b

=======
Suggestion 10

def main():
    # Get the input
    N, P, Q, R, S = map(int, input().split())
    A = list(map(int, input().split()))

    # Swap the terms
    B = A[:P-1] + A[R-1:S] + A[Q:S-R+P-1] + A[S:]

    # Print the result
    print(' '.join(map(str, B)))

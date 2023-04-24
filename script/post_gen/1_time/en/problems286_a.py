Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N, P, Q, R, S = map(int, input().split())
    A = list(map(int, input().split()))
    B = A[:P-1] + A[R-1:S] + A[Q-1:R-1] + A[S:]
    print(' '.join(map(str, B)))

=======
Suggestion 2

def swap(a, p, q, r, s):
    b = a[:p-1] + a[r-1:s] + a[q:s] + a[p-1:q-1] + a[s:]
    return b

=======
Suggestion 3

def swap(A, P, Q, R, S):
    B = []
    B.extend(A[0:P-1])
    B.extend(A[R-1:S])
    B.extend(A[Q:S])
    B.extend(A[P-1:Q-1])
    B.extend(A[S:])
    return B

N, P, Q, R, S = map(int, input().split())
A = list(map(int, input().split()))
B = swap(A, P, Q, R, S)
print(' '.join(map(str, B)))

=======
Suggestion 4

def swap(arr, p, q, r, s):
    arr[p-1:q], arr[r-1:s] = arr[r-1:s], arr[p-1:q]
    return arr

n, p, q, r, s = map(int, input().split())
arr = list(map(int, input().split()))

print(*swap(arr, p, q, r, s))

=======
Suggestion 5

def swap(p, q, r, s, a):
    b = []
    b.extend(a[:p-1])
    b.extend(a[r-1:s])
    b.extend(a[q-1:r-1])
    b.extend(a[p-1:q])
    b.extend(a[s:])
    return b

=======
Suggestion 6

def swap(a, b):
    temp = a
    a = b
    b = temp
    return a, b

=======
Suggestion 7

def swap_sequence(a, p, q, r, s):
    b = a.copy()
    for i in range(p, q+1):
        b[i-1] = a[s-i+r-2]
    for i in range(r, s+1):
        b[i-1] = a[q-i+p-2]
    return b

=======
Suggestion 8

def swap(array, start, end):
    if start == end:
        return array
    else:
        return array[:start-1] + array[end-1:start-2:-1] + array[end:]

=======
Suggestion 9

def swap(arr, p, q, r, s):
    if p > q or r > s:
        return arr
    if s - r != q - p:
        return arr
    if p < 0 or q < 0 or r < 0 or s < 0:
        return arr
    if p >= len(arr) or q >= len(arr) or r >= len(arr) or s >= len(arr):
        return arr
    if p > r:
        return arr
    if q > s:
        return arr
    if p == r and q == s:
        return arr
    if p == r and q != s:
        arr[p], arr[q+1:s+1] = arr[q+1:s+1], arr[p]
        return arr
    if p != r and q == s:
        arr[p:r+1], arr[q] = arr[q], arr[p:r+1]
        return arr
    if p != r and q != s:
        arr[p:r+1], arr[q:s+1] = arr[q:s+1], arr[p:r+1]
        return arr

=======
Suggestion 10

def swap_list(a, b, list):
    list[a:b], list[b:a] = list[b:a], list[a:b]
    return list

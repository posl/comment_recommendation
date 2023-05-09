Synthesizing 10/10 solutions

=======
Suggestion 1

def swap(a, p, q, r, s):
    b = a[:p] + a[r:s+1] + a[q+1:r] + a[p:q+1] + a[s+1:]
    return b

=======
Suggestion 2

def main():
    n, p, q, r, s = map(int, input().split())
    a = list(map(int, input().split()))
    b = a[p-1:q] + a[r-1:s]
    b.sort()
    a[p-1:q] = b[:q-p]
    a[r-1:s] = b[q-p:]
    print(*a)

=======
Suggestion 3

def main():
    n, p, q, r, s = map(int, input().split())
    a = list(map(int, input().split()))
    for i in range(n):
        if p <= i + 1 <= q or r <= i + 1 <= s:
            print(a[i], end=' ')
    for i in range(n):
        if not p <= i + 1 <= q and not r <= i + 1 <= s:
            print(a[i], end=' ')
    print()

=======
Suggestion 4

def swap(a, p, q, r, s):
    b = a[:p-1]
    b.extend(a[r-1:s])
    b.extend(a[q:s])
    b.extend(a[p-1:q])
    b.extend(a[s:])
    return b

=======
Suggestion 5

def swap(a, p, q, r, s):
    b = a.copy()
    for i in range(p-1, q):
        b[r-1+i-(q-p)] = a[i]
    for i in range(r-1, s):
        b[p-1+i-(r-q)] = a[i]
    return b

n, p, q, r, s = map(int, input().split())
a = list(map(int, input().split()))
b = swap(a, p, q, r, s)
print(*b)

=======
Suggestion 6

def swap(A, P, Q, R, S):
    B = A[:]
    for i in range(P-1, Q):
        B[i] = A[R-1+i-P]
    for i in range(R-1, S):
        B[i] = A[P-1+i-R]
    return B

=======
Suggestion 7

def swapAtoB(A, P, Q, R, S):
    A[P-1:Q], A[R-1:S] = A[R-1:S], A[P-1:Q]
    return A

=======
Suggestion 8

def swap_sequence(sequence, swap1, swap2):
    temp = sequence[swap1:swap2]
    sequence[swap1:swap2] = sequence[swap2:]
    sequence[swap2:] = temp
    return sequence

=======
Suggestion 9

def swap(a, b, c, d, e):
    return a[:b-1] + e[c-1:d] + a[b-1:c-1] + e[d:] + a[d:]

=======
Suggestion 10

def swap_list(a, start, end):
    b = a[start:end]
    a[start:end] = b[::-1]
    return a

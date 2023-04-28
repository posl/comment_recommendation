Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def swap(a, p, q, r, s):
    b = []
    b.extend(a[:p-1])
    b.extend(a[r-1:s])
    b.extend(a[q-1:r-1])
    b.extend(a[p-1:q])
    b.extend(a[s:])
    return b

=======
Suggestion 2

def swap(A, P, Q, R, S):
    B = []
    B.extend(A[0:P-1])
    B.extend(A[R-1:S])
    B.extend(A[Q:S-R+1])
    B.extend(A[P-1:Q])
    B.extend(A[S:len(A)])
    return B

=======
Suggestion 3

def swap(a, p, q, r, s):
    b = a[0:p-1] + a[r-1:s] + a[q:s] + a[p-1:q-1] + a[s:]
    return b

=======
Suggestion 4

def swap(a, p, q, r, s):
    b = a[0:p-1] + a[r-1:s] + a[q:s-1] + a[p-1:q-1] + a[s:]
    return b

=======
Suggestion 5

def swap(a, p, q, r, s):
    b = []
    for i in range(len(a)):
        if i >= p-1 and i <= q-1:
            b.append(a[i+r-q])
        elif i >= r-1 and i <= s-1:
            b.append(a[i+q-r])
        else:
            b.append(a[i])
    return b

=======
Suggestion 6

def swap(a, p, q, r, s):
    b = a[:]
    for i in range(p-1, q):
        b[i] = a[r-1+i-q]
    for i in range(r-1, s):
        b[i] = a[p-1+i-r]
    return b

=======
Suggestion 7

def swap(p,q,r,s,a):
    b = list(a)
    for i in range(p-1,q):
        b[i] = a[i+r-q]
    for i in range(r-1,s):
        b[i] = a[i+q-p]
    return b

n,p,q,r,s = map(int,input().split())
a = list(map(int,input().split()))
b = swap(p,q,r,s,a)
print(' '.join([str(x) for x in b]))

=======
Suggestion 8

def swapper(list, p, q, r, s):
    p = p - 1
    q = q - 1
    r = r - 1
    s = s - 1
    for i in range(q - p + 1):
        list[p + i], list[s - i] = list[s - i], list[p + i]
    return list

=======
Suggestion 9

def swap(a, b):
    return b, a

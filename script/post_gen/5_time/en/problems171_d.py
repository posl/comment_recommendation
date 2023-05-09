Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N = int(input())
    A = list(map(int, input().split()))
    Q = int(input())
    B = []
    C = []
    for i in range(Q):
        b, c = map(int, input().split())
        B.append(b)
        C.append(c)
    A.sort()
    for i in range(Q):
        if B[i] in A:
            A = [C[i] if x == B[i] else x for x in A]
            A.sort()
        print(sum(A))

=======
Suggestion 2

def main():
    n = int(input())
    a = list(map(int, input().split()))
    q = int(input())
    bc = [list(map(int, input().split())) for _ in range(q)]
    s = sum(a)
    d = {}
    for i in a:
        if i in d:
            d[i] += 1
        else:
            d[i] = 1
    for b, c in bc:
        if b in d:
            s += (c - b) * d[b]
            if c in d:
                d[c] += d[b]
            else:
                d[c] = d[b]
            del d[b]
        print(s)

=======
Suggestion 3

def main():
    n = int(input())
    a = list(map(int, input().split()))
    q = int(input())
    b = []
    c = []
    for i in range(q):
        b_i, c_i = map(int, input().split())
        b.append(b_i)
        c.append(c_i)
    a_sum = sum(a)
    b_sum = dict(zip(range(1, n+1), a))
    for i in range(q):
        a_sum += (c[i] - b[i]) * b_sum[b[i]]
        print(a_sum)
        b_sum[c[i]] = b_sum.get(c[i], 0) + b_sum[b[i]]
        b_sum[b[i]] = 0

=======
Suggestion 4

def main():
    N = int(input())
    A = list(map(int, input().split()))
    Q = int(input())
    BC = [list(map(int, input().split())) for _ in range(Q)]

    total = sum(A)
    count = {}
    for a in A:
        if a in count:
            count[a] += 1
        else:
            count[a] = 1

    for b, c in BC:
        if b in count:
            total += (c - b) * count[b]
            if c in count:
                count[c] += count[b]
            else:
                count[c] = count[b]
            count[b] = 0
        print(total)

=======
Suggestion 5

def main():
    n = int(input())
    a = list(map(int, input().split()))
    q = int(input())
    bc = []
    for i in range(q):
        bc.append(list(map(int, input().split())))
    a.sort()
    s = sum(a)
    for i in range(q):
        s += (bc[i][1] - bc[i][0]) * a.count(bc[i][0])
        print(s)
        a = list(map(lambda x: bc[i][1] if x == bc[i][0] else x, a))

=======
Suggestion 6

def main():
    N = int(input())
    A = list(map(int, input().split()))
    Q = int(input())
    BC = [list(map(int, input().split())) for _ in range(Q)]

    A = [0] + A
    S = sum(A)
    D = {}
    for i in range(1, N+1):
        D[i] = A[i]

    for b, c in BC:
        S += (c - b) * D[b]
        D[c] += D[b]
        D[b] = 0
        print(S)

=======
Suggestion 7

def main():
    N = int(input())
    A = list(map(int,input().split()))
    Q = int(input())
    BC = [list(map(int,input().split())) for i in range(Q)]
    S = sum(A)
    for i in range(Q):
        B,C = BC[i]
        S += (C-B)*A.count(B)
        print(S)
        A = [C if A[i]==B else A[i] for i in range(N)]

=======
Suggestion 8

def main():
    # Get number of elements in the list
    n = int(input())

    # Get the list
    a = list(map(int, input().split()))

    # Get number of operations to be performed
    q = int(input())

    # Get the list of operations
    b = list()
    c = list()
    for i in range(q):
        b.append(int(input()))
        c.append(int(input()))

    # Perform the operations
    for i in range(q):
        for j in range(n):
            if a[j] == b[i]:
                a[j] = c[i]

        print(sum(a))

=======
Suggestion 9

def get_sum(arr):
    sum = 0
    for i in arr:
        sum += i
    return sum

=======
Suggestion 10

def read_int_list():
    return [int(x) for x in input().split()]

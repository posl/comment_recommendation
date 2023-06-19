Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    n = int(input())
    a = list(map(int, input().split()))
    q = int(input())
    b = []
    c = []
    for i in range(q):
        b1, c1 = map(int, input().split())
        b.append(b1)
        c.append(c1)
    sum = 0
    for i in range(n):
        sum += a[i]
    for i in range(q):
        sum += (c[i] - b[i]) * a.count(b[i])
        print(sum)
        for j in range(n):
            if a[j] == b[i]:
                a[j] = c[i]
        #print(a)

=======
Suggestion 2

def main():
    n = int(input())
    a = list(map(int, input().split()))
    q = int(input())
    b = []
    c = []
    for i in range(q):
        b1, c1 = map(int, input().split())
        b.append(b1)
        c.append(c1)
    s = sum(a)
    for i in range(q):
        s = s + (c[i] - b[i]) * a.count(b[i])
        print(s)

=======
Suggestion 3

def main():
    n = int(input())
    A = list(map(int, input().split()))
    q = int(input())
    B = []
    C = []
    for i in range(q):
        b, c = map(int, input().split())
        B.append(b)
        C.append(c)

    sum = 0
    for i in range(n):
        sum += A[i]

    for i in range(q):
        sum += (C[i] - B[i]) * A.count(B[i])
        print(sum)
        sum = sum - (C[i] - B[i]) * A.count(B[i])
        A = list(map(lambda x: C[i] if x == B[i] else x, A))

=======
Suggestion 4

def main():
    n = int(input())
    a_list = list(map(int, input().split()))
    q = int(input())
    bc_list = [list(map(int, input().split())) for _ in range(q)]

    sum_a = sum(a_list)
    d = {}
    for a in a_list:
        if a in d:
            d[a] += 1
        else:
            d[a] = 1

    for b, c in bc_list:
        if b in d:
            sum_a += (c - b) * d[b]
            if c in d:
                d[c] += d[b]
            else:
                d[c] = d[b]
            d.pop(b)
        print(sum_a)

=======
Suggestion 5

def main():
    N = int(input())
    A = list(map(int, input().split()))
    Q = int(input())
    BC = [list(map(int, input().split())) for _ in range(Q)]
    print(N, A, Q, BC)
    for i in range(Q):
        B = BC[i][0]
        C = BC[i][1]
        for j in range(N):
            if A[j] == B:
                A[j] = C
        print(sum(A))

=======
Suggestion 6

def main():
    n = int(input())
    a = list(map(int, input().split()))
    q = int(input())
    bc = []
    for _ in range(q):
        bc.append(list(map(int, input().split())))
    s = sum(a)
    for b, c in bc:
        s += (c - b) * a.count(b)
        print(s)
        a = list(map(lambda x: c if x == b else x, a))

=======
Suggestion 7

def main():
    n = int(input())
    a = list(map(int, input().split()))
    q = int(input())
    b = []
    c = []
    for i in range(q):
        b_temp, c_temp = map(int, input().split())
        b.append(b_temp)
        c.append(c_temp)

    sum_a = sum(a)
    for i in range(q):
        sum_a += (c[i] - b[i]) * a.count(b[i])
        print(sum_a)
        sum_a -= (c[i] - b[i]) * a.count(b[i])

=======
Suggestion 8

def solve():
    n = int(input())
    a = list(map(int, input().split()))
    q = int(input())
    bc = [list(map(int, input().split())) for _ in range(q)]

    sum_a = sum(a)
    cnt = [0] * 10**5
    for i in range(n):
        cnt[a[i]-1] += 1

    for i in range(q):
        sum_a += (bc[i][1]-bc[i][0]) * cnt[bc[i][0]-1]
        cnt[bc[i][1]-1] += cnt[bc[i][0]-1]
        cnt[bc[i][0]-1] = 0
        print(sum_a)

=======
Suggestion 9

def solve():
    n = int(input())
    a = [int(i) for i in input().split()]
    q = int(input())
    b = []
    c = []
    for i in range(q):
        b_i, c_i = [int(i) for i in input().split()]
        b.append(b_i)
        c.append(c_i)

    # print(n)
    # print(a)
    # print(q)
    # print(b)
    # print(c)

    sum_a = sum(a)
    # print(sum_a)

    for i in range(q):
        sum_a = sum_a - a.count(b[i]) * b[i] + a.count(b[i]) * c[i]
        print(sum_a)

solve()

Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N = int(input())
    A = list(map(int, input().split()))
    Q = int(input())
    BC = [list(map(int, input().split())) for _ in range(Q)]
    print(N, A, Q, BC)

=======
Suggestion 2

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
    count = []
    for i in range(q):
        count.append(a.count(b[i]))
        a_sum += (c[i] - b[i]) * count[i]
        print(a_sum)

=======
Suggestion 3

def main():
    N = int(input())
    A = [int(x) for x in input().split()]
    Q = int(input())
    BC = [[int(x) for x in input().split()] for _ in range(Q)]
    A_sum = sum(A)
    B_sum = [0] * (10 ** 5 + 1)
    for a in A:
        B_sum[a] += 1
    for b, c in BC:
        A_sum += (c - b) * B_sum[b]
        B_sum[c] += B_sum[b]
        B_sum[b] = 0
        print(A_sum)

=======
Suggestion 4

def main():
    N = int(input())
    A = list(map(int, input().split()))
    Q = int(input())
    BC = [list(map(int, input().split())) for i in range(Q)]
    print(A, BC)
    B = [BC[i][0] for i in range(Q)]
    C = [BC[i][1] for i in range(Q)]
    print(B, C)
    print(A)
    for i in range(Q):
        A = list(map(lambda x:x if x != B[i] else C[i], A))
        print(A)
        print(sum(A))

=======
Suggestion 5

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
        sum = sum - (a.count(b[i]) * b[i]) + (a.count(b[i]) * c[i])
        print(sum)

=======
Suggestion 6

def main():
    N = int(input())
    A = list(map(int, input().split()))
    Q = int(input())
    BC = [list(map(int, input().split())) for _ in range(Q)]

    sum_A = sum(A)
    cnt = [0] * (10**5 + 1)
    for a in A:
        cnt[a] += 1

    for b, c in BC:
        sum_A += (c - b) * cnt[b]
        cnt[c] += cnt[b]
        cnt[b] = 0
        print(sum_A)

=======
Suggestion 7

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
    for i in range(q):
        a_sum += (c[i]-b[i])*a.count(b[i])
        print(a_sum)
        a = [c[i] if a_i == b[i] else a_i for a_i in a]

=======
Suggestion 8

def main():
    n = int(input())
    a = list(map(int, input().split()))
    q = int(input())
    b = [0 for _ in range(q)]
    c = [0 for _ in range(q)]
    for i in range(q):
        b[i], c[i] = map(int, input().split())
    sum = 0
    for i in range(n):
        sum += a[i]
    for i in range(q):
        sum += (c[i] - b[i]) * a.count(b[i])
        print(sum)
        sum = 0

=======
Suggestion 9

def main():
    num = int(input())
    a = list(map(int, input().split()))
    q = int(input())
    bc = []
    for i in range(q):
        bc.append(list(map(int, input().split())))
    sum = 0
    for i in range(num):
        sum += a[i]
    for i in range(q):
        sum = sum + bc[i][1] * a.count(bc[i][0]) - bc[i][0] * a.count(bc[i][0])
        print(sum)

=======
Suggestion 10

def main():
    N = int(input())
    A = list(map(int, input().split()))
    Q = int(input())
    BC = [list(map(int, input().split())) for _ in range(Q)]
    sum = 0
    for a in A:
        sum += a
    for bc in BC:
        sum += (bc[1] - bc[0]) * A.count(bc[0])
        print(sum)
        sum += (bc[0] - bc[1]) * A.count(bc[0])
        for i in range(N):
            if A[i] == bc[0]:
                A[i] = bc[1]

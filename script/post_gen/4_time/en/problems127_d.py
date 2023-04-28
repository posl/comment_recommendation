Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    A.sort()
    BC = [list(map(int, input().split())) for _ in range(M)]
    BC.sort(key=lambda x: x[1], reverse=True)
    i = 0
    for b, c in BC:
        for _ in range(b):
            if i >= N:
                break
            if A[i] < c:
                A[i] = c
            else:
                break
            i += 1
    print(sum(A))

=======
Suggestion 2

def main():
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    bc = [list(map(int, input().split())) for _ in range(m)]
    a.sort()
    bc.sort(key=lambda x: -x[1])
    b = [0] * m
    c = [0] * m
    for i in range(m):
        b[i] = bc[i][0]
        c[i] = bc[i][1]
    i = 0
    j = 0
    while i < n and j < m:
        if a[i] < c[j]:
            a[i] = c[j]
            b[j] -= 1
            if b[j] == 0:
                j += 1
        i += 1
    print(sum(a))

=======
Suggestion 3

def main():
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    a.sort()
    bc = [list(map(int, input().split())) for _ in range(m)]
    bc.sort(key=lambda x: x[1], reverse=True)
    i = 0
    for b, c in bc:
        for _ in range(b):
            if i >= n or c <= a[i]:
                break
            a[i] = c
            i += 1
        if i >= n:
            break
    print(sum(a))

=======
Suggestion 4

def main():
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    a.sort()
    bc = [list(map(int, input().split())) for _ in range(m)]
    bc.sort(key=lambda x: x[1], reverse=True)
    i = 0
    for b, c in bc:
        for _ in range(b):
            if i >= n or a[i] >= c:
                break
            a[i] = c
            i += 1
        else:
            continue
        break
    print(sum(a))

=======
Suggestion 5

def main():
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    a.sort(reverse=True)
    bc = [list(map(int, input().split())) for _ in range(m)]
    bc.sort(key=lambda x: x[1], reverse=True)
    idx = 0
    for b, c in bc:
        for _ in range(b):
            if idx >= n or c <= a[idx]:
                break
            a[idx] = c
            idx += 1
    print(sum(a))

=======
Suggestion 6

def main():
    N,M = map(int, input().split())
    A = list(map(int, input().split()))
    BC = []
    for _ in range(M):
        BC.append(list(map(int, input().split())))
    BC.sort(key=lambda x: x[1], reverse=True)
    for i in range(M):
        if BC[i][0] >= N:
            for j in range(N):
                A[j] = BC[i][1]
            break
        else:
            for j in range(BC[i][0]):
                A[j] = BC[i][1]
            N -= BC[i][0]
    print(sum(A))

=======
Suggestion 7

def solve(n, m, a, b, c):
    a.sort()
    for i in range(m):
        for j in range(b[i]):
            if a[j] < c[i]:
                a[j] = c[i]
            else:
                break
        a.sort()
    return sum(a)

n, m = map(int, input().split())
a = list(map(int, input().split()))
b = []
c = []
for i in range(m):
    b_i, c_i = map(int, input().split())
    b.append(b_i)
    c.append(c_i)
print(solve(n, m, a, b, c))

=======
Suggestion 8

def main():
    # get input
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    b = []
    c = []
    for i in range(m):
        b_i, c_i = map(int, input().split())
        b.append(b_i)
        c.append(c_i)

    # solve
    a.sort(reverse=True)
    b_c = list(zip(b, c))
    b_c.sort(key=lambda x: x[1], reverse=True)
    i = 0
    j = 0
    while i < n and j < m:
        if a[i] < b_c[j][1]:
            a[i] = b_c[j][1]
            b_c[j][0] -= 1
            if b_c[j][0] == 0:
                j += 1
        else:
            break
        i += 1

    # output
    print(sum(a))

=======
Suggestion 9

def maximum_sum_of_cards(N, M, A, B, C):
    A.sort()
    operations = sorted(zip(B, C), key=lambda x: x[1], reverse=True)
    i = 0
    for b, c in operations:
        if A[i] < c:
            for j in range(b):
                if A[i] >= c:
                    break
                A[i] = c
                i += 1
    return sum(A)

=======
Suggestion 10

def checkSum(cards):
    sum = 0
    for card in cards:
        sum += card
    return sum

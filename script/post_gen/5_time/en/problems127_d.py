Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    BC = []
    for i in range(M):
        BC.append(list(map(int, input().split())))
    A.sort()
    BC.sort(key=lambda x: x[1], reverse=True)
    j = 0
    for i in range(N):
        if j < M and A[i] < BC[j][1]:
            A[i] = BC[j][1]
            BC[j][0] -= 1
            if BC[j][0] == 0:
                j += 1
        else:
            break
    print(sum(A))

=======
Suggestion 2

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
Suggestion 3

def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    A.sort()
    BC = []
    for _ in range(M):
        BC.append(list(map(int, input().split())))
    BC.sort(key=lambda x: x[1], reverse=True)

    A = A[::-1]
    BC = BC[::-1]
    i = 0
    j = 0
    while i < N and j < M:
        if BC[j][0] == 0:
            j += 1
        else:
            A[i] = BC[j][1]
            BC[j][0] -= 1
            i += 1
    print(sum(A))

=======
Suggestion 4

def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    A.sort()
    BC = []
    for _ in range(M):
        b, c = map(int, input().split())
        BC.append((b, c))
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
Suggestion 5

def solve():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    BC = [list(map(int, input().split())) for i in range(M)]
    A.sort()
    BC.sort(key=lambda x: x[1], reverse=True)
    i = 0
    for b, c in BC:
        while b > 0 and i < N and c > A[i]:
            A[i] = c
            i += 1
            b -= 1
        if b == 0:
            break
    print(sum(A))

=======
Suggestion 6

def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    A.sort()
    BC = []
    for i in range(M):
        BC.append(tuple(map(int, input().split())))
    BC.sort(key=lambda x: x[1], reverse=True)
    i = 0
    for b, c in BC:
        for j in range(b):
            if i >= N or A[i] >= c:
                break
            A[i] = c
            i += 1
        else:
            continue
        break
    print(sum(A))

=======
Suggestion 7

def main():
    n,m = map(int, input().split())
    a = list(map(int, input().split()))
    bc = []
    for _ in range(m):
        b,c = map(int, input().split())
        bc.append([b,c])
    a.sort()
    bc.sort(key=lambda x:x[1], reverse=True)
    i = 0
    for b,c in bc:
        for _ in range(b):
            if a[i] >= c:
                break
            a[i] = c
            i += 1
            if i == n:
                break
        if i == n:
            break
    print(sum(a))

=======
Suggestion 8

def maximum_sum_of_integers(N, M, A, B, C):
    A.sort()
    B.sort(key=lambda x: x[1], reverse=True)
    i = 0
    j = 0
    while i < N and j < M:
        if A[i] < B[j][1]:
            A[i] = B[j][1]
            j += 1
        else:
            break
    return sum(A)

=======
Suggestion 9

def get_sum_of_cards(N, M, A, BC):
    A.sort()
    BC.sort(key=lambda x: x[1], reverse=True)
    cards = A
    for i in range(M):
        b = BC[i][0]
        c = BC[i][1]
        for j in range(b):
            if cards[j] < c:
                cards[j] = c
            else:
                break
        cards.sort()
    return sum(cards)

=======
Suggestion 10

def read_ints():
	return list(map(int, input().split()))

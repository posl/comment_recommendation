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
        if j == M:
            break
        if A[i] < BC[j][1]:
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
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    BC = []
    for _ in range(M):
        BC.append(list(map(int, input().split())))
    A.sort()
    BC.sort(key=lambda x: x[1], reverse=True)
    BC = BC[:N]
    i = 0
    for j in range(N):
        if A[j] < BC[i][1]:
            A[j] = BC[i][1]
            BC[i][0] -= 1
            if BC[i][0] == 0:
                i += 1
            if i == M:
                break
    print(sum(A))

=======
Suggestion 3

def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    BC = []
    for _ in range(M):
        BC.append(list(map(int, input().split())))

    A.sort(reverse = True)
    BC.sort(key = lambda x: x[1], reverse = True)
    card = 0
    for b, c in BC:
        for _ in range(b):
            if card >= N:
                break
            if A[card] < c:
                A[card] = c
                card += 1
            else:
                break
    print(sum(A))

=======
Suggestion 4

def main():
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    a.sort()
    bc = [list(map(int, input().split())) for _ in range(m)]
    bc.sort(key = lambda x: x[1], reverse = True)
    i = 0
    for b, c in bc:
        for j in range(b):
            if a[i] < c:
                a[i] = c
                i += 1
            else:
                break
            if i >= n:
                break
        if i >= n:
            break
    print(sum(a))

=======
Suggestion 5

def main():
    n, m = map(int, input().split())
    a_list = list(map(int, input().split()))
    bc_list = []
    for _ in range(m):
        b, c = map(int, input().split())
        bc_list.append((b, c))

    a_list.sort(reverse=True)
    bc_list.sort(key=lambda x: x[1], reverse=True)

    i = 0
    j = 0
    while i < n and j < m:
        if a_list[i] < bc_list[j][1]:
            a_list[i] = bc_list[j][1]
            bc_list[j] = (bc_list[j][0] - 1, bc_list[j][1])
            if bc_list[j][0] == 0:
                j += 1
        else:
            break
        i += 1

    print(sum(a_list))

=======
Suggestion 6

def main():
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    a.sort(reverse=True)
    bc = [list(map(int, input().split())) for _ in range(m)]
    bc.sort(key=lambda x: x[1], reverse=True)
    i = 0
    j = 0
    while i < n and j < m:
        if a[i] < bc[j][1]:
            a[i] = bc[j][1]
            bc[j][0] -= 1
            if bc[j][0] == 0:
                j += 1
        i += 1
    print(sum(a))

=======
Suggestion 7

def main():
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    a.sort()
    b = []
    for i in range(m):
        b.append(list(map(int, input().split())))
    b.sort(key=lambda x:x[1], reverse=True)
    j = 0
    for i in range(n):
        if j == m:
            break
        if a[i] < b[j][1]:
            a[i] = b[j][1]
            b[j][0] -= 1
            if b[j][0] == 0:
                j += 1
        else:
            break
    print(sum(a))

=======
Suggestion 8

def solve():
    N,M = map(int,input().split())
    A = list(map(int,input().split()))
    BC = [list(map(int,input().split())) for _ in range(M)]
    A.sort()
    BC.sort(key=lambda x:x[1],reverse=True)
    i = 0
    for j in range(M):
        for k in range(BC[j][0]):
            if A[i] < BC[j][1]:
                A[i] = BC[j][1]
                i += 1
            else:
                break
    print(sum(A))

=======
Suggestion 9

def main():
    n,m = map(int,input().split())
    a = list(map(int,input().split()))
    bc = [list(map(int,input().split())) for _ in range(m)]

    a.sort()
    bc.sort(key=lambda x:x[1],reverse=True)

    i = 0
    for b,c in bc:
        for _ in range(b):
            if a[i] < c:
                a[i] = c
                i += 1
            else:
                break
            if i >= n:
                break
        else:
            continue
        break

    print(sum(a))

=======
Suggestion 10

def solve():
    N,M = map(int,input().split())
    A = list(map(int,input().split()))
    BC = [list(map(int,input().split())) for _ in range(M)]

    A.sort()
    BC.sort(key=lambda x:x[1],reverse=True)

    idx = 0
    for i in range(M):
        for _ in range(BC[i][0]):
            if idx >= N:
                break
            if A[idx] < BC[i][1]:
                A[idx] = BC[i][1]
                idx += 1
            else:
                break
        if idx >= N:
            break
    print(sum(A))

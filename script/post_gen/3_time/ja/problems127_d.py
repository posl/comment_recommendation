Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    BC = [list(map(int, input().split())) for _ in range(M)]
    A.sort()
    BC.sort(key=lambda x:x[1], reverse=True)
    i = 0
    j = 0
    while i < N and j < M:
        if A[i] < BC[j][1]:
            A[i] = BC[j][1]
            BC[j][0] -= 1
            if BC[j][0] == 0:
                j += 1
            i += 1
        else:
            break
    print(sum(A))

=======
Suggestion 2

def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    BC = [list(map(int, input().split())) for i in range(M)]
    A.sort()
    BC.sort(key=lambda x: x[1], reverse=True)
    i = 0
    for j in range(M):
        while BC[j][0] > 0 and i < N and A[i] < BC[j][1]:
            A[i] = BC[j][1]
            BC[j][0] -= 1
            i += 1
    print(sum(A))

=======
Suggestion 3

def main():
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    bc = [list(map(int, input().split())) for _ in range(m)]

    a.sort()
    bc.sort(key=lambda x: x[1], reverse=True)

    i = 0
    for b, c in bc:
        while b > 0 and i < n and a[i] < c:
            a[i] = c
            i += 1
            b -= 1
        if b == 0:
            break

    print(sum(a))

=======
Suggestion 4

def main():
    N,M = map(int,input().split())
    A = list(map(int,input().split()))
    BC = []
    for i in range(M):
        BC.append(list(map(int,input().split())))
    A.sort()
    BC.sort(key=lambda x: x[1], reverse=True)
    i = 0
    j = 0
    while i < N and j < M:
        if A[i] < BC[j][1]:
            A[i] = BC[j][1]
            BC[j][0] -= 1
            if BC[j][0] == 0:
                j += 1
            i += 1
        else:
            break
    print(sum(A))

=======
Suggestion 5

def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))

    BC = []
    for _ in range(M):
        BC.append(list(map(int, input().split())))

    A.sort()
    BC.sort(key=lambda x: x[1], reverse=True)

    i = 0
    j = 0
    while i < N and j < M:
        if A[i] < BC[j][1]:
            A[i] = BC[j][1]
            BC[j][0] -= 1
            if BC[j][0] == 0:
                j += 1
            i += 1
        else:
            break

    print(sum(A))

=======
Suggestion 6

def main():
    N,M = map(int,input().split())
    A = list(map(int,input().split()))
    BC = [list(map(int,input().split())) for _ in range(M)]
    A.sort()
    BC.sort(key=lambda x:x[1],reverse=True)
    i = 0
    j = 0
    while i < N and j < M:
        if A[i] < BC[j][1]:
            A[i] = BC[j][1]
            BC[j][0] -= 1
            if BC[j][0] == 0:
                j += 1
        else:
            break
        i += 1
    print(sum(A))

=======
Suggestion 7

def main():
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    a.sort(reverse=True)
    bc = []
    for i in range(m):
        b, c = map(int, input().split())
        bc.append([b,c])
    bc.sort(key=lambda x: x[1], reverse=True)
    j = 0
    for i in range(n):
        if j < m and a[i] < bc[j][1]:
            a[i] = bc[j][1]
            bc[j][0] -= 1
            if bc[j][0] == 0:
                j += 1
        else:
            break
    print(sum(a))

=======
Suggestion 8

def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    BC = [list(map(int, input().split())) for _ in range(M)]
    
    A.sort(reverse=True)
    BC.sort(key=lambda x: x[1], reverse=True)
    
    i = 0
    j = 0
    while i < N and j < M:
        if A[i] < BC[j][1]:
            A[i] = BC[j][1]
            BC[j][0] -= 1
            if BC[j][0] == 0:
                j += 1
        i += 1
    
    print(sum(A))

=======
Suggestion 9

def main():
    N,M = map(int,input().split())
    A = list(map(int,input().split()))
    BC = [list(map(int,input().split())) for _ in range(M)]

    A.sort()
    BC.sort(key=lambda x: x[1], reverse=True)

    idx = 0
    for i in range(M):
        for _ in range(BC[i][0]):
            if A[idx] < BC[i][1]:
                A[idx] = BC[i][1]
                idx += 1
                if idx == N:
                    break
            else:
                break
        if idx == N:
            break

    print(sum(A))

=======
Suggestion 10

def main():
    # input
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    BC = []
    for i in range(M):
        BC.append(list(map(int, input().split())))
    # compute
    A.sort()
    BC.sort(key=lambda x: x[1], reverse=True)
    i, j = 0, 0
    while i<N and j<M:
        if A[i] < BC[j][1]:
            A[i] = BC[j][1]
            BC[j][0] -= 1
            if BC[j][0] == 0:
                j += 1
            i += 1
        else:
            break
    # output
    print(sum(A))

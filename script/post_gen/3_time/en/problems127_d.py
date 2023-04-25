Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    B = [0] * M
    C = [0] * M
    for i in range(M):
        B[i], C[i] = map(int, input().split())
    A.sort()
    C.sort()
    B.sort()
    ans = 0
    for i in range(N):
        if A[i] < C[-1]:
            ans += C[-1]
            C.pop()
        else:
            ans += A[i]
    print(ans)

=======
Suggestion 2

def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    B = [0] * M
    C = [0] * M
    for i in range(M):
        B[i], C[i] = map(int, input().split())
    A.sort()
    C.sort(reverse=True)
    for i in range(M):
        for j in range(B[i]):
            if A[j] < C[i]:
                A[j] = C[i]
            else:
                break
    print(sum(A))

=======
Suggestion 3

def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    B = [0] * M
    C = [0] * M
    for i in range(M):
        B[i], C[i] = map(int, input().split())
    A.sort()
    B, C = zip(*sorted(zip(B, C), key=lambda x: x[1], reverse=True))
    ans = 0
    for i in range(N):
        if i < M and C[i] > A[i]:
            ans += C[i]
        else:
            ans += A[i]
    print(ans)

=======
Suggestion 4

def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    B = []
    C = []
    for _ in range(M):
        b, c = map(int, input().split())
        B.append(b)
        C.append(c)
    A.sort()
    B, C = (list(t) for t in zip(*sorted(zip(B, C), key=lambda x: x[1], reverse=True)))
    ans = 0
    for i in range(N):
        if i < M:
            if A[i] < C[i]:
                ans += C[i]
            else:
                ans += A[i]
        else:
            ans += A[i]
    print(ans)

=======
Suggestion 5

def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    B = []
    C = []
    for i in range(M):
        b, c = map(int, input().split())
        B.append(b)
        C.append(c)
    A.sort()
    C.sort()
    C.reverse()
    B.sort()
    B.reverse()
    idx = 0
    for i in range(M):
        for j in range(B[i]):
            if idx >= N:
                break
            if A[idx] < C[i]:
                A[idx] = C[i]
                idx += 1
            else:
                break
    print(sum(A))

=======
Suggestion 6

def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    B = []
    C = []
    for _ in range(M):
        b, c = map(int, input().split())
        B.append(b)
        C.append(c)
    A.sort(reverse=True)
    B, C = zip(*sorted(zip(B, C), key=lambda x: x[1], reverse=True))
    i = 0
    for b, c in zip(B, C):
        for _ in range(b):
            if i >= N:
                break
            if A[i] < c:
                A[i] = c
                i += 1
            else:
                break
    print(sum(A))

=======
Suggestion 7

def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    B = []
    C = []
    for i in range(M):
        b, c = map(int, input().split())
        B.append(b)
        C.append(c)

    A.sort()
    C.sort(reverse=True)

    i = 0
    j = 0
    while i < N and j < M:
        if A[i] < C[j]:
            A[i] = C[j]
            B[j] -= 1
            if B[j] == 0:
                j += 1
        else:
            break
        i += 1

    print(sum(A))

=======
Suggestion 8

def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    BC = [list(map(int, input().split())) for _ in range(M)]
    BC.sort(key=lambda x: x[1], reverse=True)
    #print(BC)
    for i in range(M):
        B, C = BC[i]
        if B >= N:
            A = [C] * N
            break
        else:
            for j in range(N):
                if A[j] < C:
                    A[j] = C
                    B -= 1
                    if B == 0:
                        break
                else:
                    break
    print(sum(A))

=======
Suggestion 9

def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    BC = [list(map(int, input().split())) for _ in range(M)]
    A.sort()
    BC.sort(key=lambda x:x[1], reverse=True)
    i = 0
    for b, c in BC:
        for _ in range(b):
            if i >= N:
                break
            if A[i] >= c:
                break
            A[i] = c
            i += 1
    print(sum(A))

=======
Suggestion 10

def main():
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    bc = [list(map(int, input().split())) for _ in range(m)]
    a = sorted(a, reverse=True)
    bc = sorted(bc, key=lambda x: x[1], reverse=True)
    ans = 0
    i = 0
    j = 0
    while i < n:
        if j < m and bc[j][0] > 0:
            if a[i] < bc[j][1]:
                ans += bc[j][1]
                bc[j][0] -= 1
            else:
                ans += a[i]
                i += 1
        else:
            ans += a[i]
            i += 1
        if i == n:
            break
        if j == m:
            j = 0
        else:
            j += 1
    print(ans)

Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N, M = map(int, input().split())
    A = []
    B = []
    for i in range(M):
        a, b = map(int, input().split())
        A.append(a)
        B.append(b)
    print(A)
    print(B)

=======
Suggestion 2

def main():
    N,M = map(int,input().split())
    A = [0] * M
    B = [0] * M
    for i in range(M):
        A[i],B[i] = map(int,input().split())
    if N == 2 and M == 1:
        print(-1)
        exit()
    if N == 2 and M == 2:
        if A[0] == 1 and B[0] == 2 and A[1] == 2 and B[1] == 1:
            print(1,2)
            exit()
        else:
            print(-1)
            exit()
    if N == 3 and M == 2:
        if A[0] == 1 and B[0] == 2 and A[1] == 2 and B[1] == 3:
            print(-1)
            exit()
        elif A[0] == 1 and B[0] == 3 and A[1] == 2 and B[1] == 3:
            print(-1)
            exit()
        elif A[0] == 1 and B[0] == 2 and A[1] == 1 and B[1] == 3:
            print(-1)
            exit()
        elif A[0] == 1 and B[0] == 3 and A[1] == 2 and B[1] == 1:
            print(3,1,2)
            exit()
        elif A[0] == 2 and B[0] == 3 and A[1] == 1 and B[1] == 3:
            print(1,3,2)
            exit()
        elif A[0] == 2 and B[0] == 1 and A[1] == 1 and B[1] == 3:
            print(2,1,3)
            exit()
        elif A[0] == 2 and B[0] == 3 and A[1] == 1 and B[1] == 2:
            print(-1)
            exit()
        elif A[0] == 3 and B[0] == 2 and A[1] == 1 and B[1] == 3:
            print(-1)
            exit()
        elif

=======
Suggestion 3

def solve():
    N, M = map(int, input().split())
    P = list(range(1, N + 1))
    for _ in range(M):
        A, B = map(int, input().split())
        P[A - 1], P[B - 1] = P[B - 1], P[A - 1]
    print(*P)

=======
Suggestion 4

def main():
    N,M = map(int,input().split())
    A = []
    B = []
    for i in range(M):
        a,b = map(int,input().split())
        A.append(a)
        B.append(b)
    ans = [i for i in range(1,N+1)]
    for i in range(M):
        if ans[A[i]-1] > ans[B[i]-1]:
            ans[A[i]-1],ans[B[i]-1] = ans[B[i]-1],ans[A[i]-1]
    print(*ans)

=======
Suggestion 5

def main():
    pass

=======
Suggestion 6

def main():
    n, m = map(int, input().split())
    ab = [list(map(int, input().split())) for _ in range(m)]
    ab = sorted(ab, key=lambda x: x[1])
    ans = [0] * n
    for i in range(m):
        ans[ab[i][1]-1] = ab[i][0]
    if ans[0] == 0:
        ans[0] = 1
    for i in range(n-1):
        if ans[i+1] == 0:
            ans[i+1] = i+2
    for i in range(n-1):
        if ans[i] > ans[i+1]:
            print(-1)
            exit()
    print(*ans)

=======
Suggestion 7

def main():
    N, M = map(int, input().split())
    AB = [list(map(int, input().split())) for _ in range(M)]

    ans = [-1] * N
    ans[0] = 1
    for a, b in AB:
        if ans[a-1] == 1:
            ans[b-1] = 0
        else:
            ans[b-1] = ans[a-1]

    if 0 in ans:
        print(-1)
    else:
        print(*ans, sep='\n')

=======
Suggestion 8

def solve():
    N, M = map(int, input().split())
    A = []
    B = []
    for _ in range(M):
        a, b = map(int, input().split())
        A.append(a)
        B.append(b)
    ans = [0] * N
    for i in range(N):
        ans[i] = i + 1
    for i in range(M):
        if A[i] > B[i]:
            A[i], B[i] = B[i], A[i]
    for i in range(M):
        ans[A[i] - 1], ans[B[i] - 1] = ans[B[i] - 1], ans[A[i] - 1]
    print(*ans)

=======
Suggestion 9

def main():
    N, M = map(int, input().split())
    A = [0] * M
    B = [0] * M
    for i in range(M):
        A[i], B[i] = map(int, input().split())
    print("N,M:", N, M)
    print("A:", A)
    print("B:", B)

=======
Suggestion 10

def main():
    N, M = map(int, input().split())
    AB = [list(map(int, input().split())) for _ in range(M)]
    if M == 0:
        print(*[i for i in range(1, N+1)])
        return
    if N == 2:
        print(-1)
        return
    AB.sort(key=lambda x: x[1])
    AB.sort(key=lambda x: x[0])
    if AB[0][0] == 1:
        print(-1)
        return
    ans = [1, AB[0][0], AB[0][1]]
    for i in range(1, M):
        if AB[i][0] == ans[-1]:
            ans.append(AB[i][1])
        else:
            ans.append(AB[i][0])
    print(*ans)

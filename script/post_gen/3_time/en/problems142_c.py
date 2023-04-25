Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    N = int(input())
    A = list(map(int, input().split()))
    B = [0] * N
    for i in range(N):
        B[A[i] - 1] = i + 1
    print(*B)

=======
Suggestion 2

def main():
    n = int(input())
    a = list(map(int, input().split()))
    b = [0] * n
    for i in range(n):
        b[a[i] - 1] = i + 1
    print(' '.join(map(str, b)))

=======
Suggestion 3

def main():
    N = int(input())
    A = list(map(int,input().split()))
    ans = [0]*N
    for i in range(N):
        ans[A[i]-1] = i+1
    print(" ".join(map(str,ans)))

=======
Suggestion 4

def main():
    N = int(input())
    A = [int(a) for a in input().split()]
    B = [0] * N
    for i in range(N):
        B[A[i] - 1] = i + 1
    print(' '.join(str(b) for b in B))

=======
Suggestion 5

def solve():
    N = int(input())
    A = list(map(int,input().split()))
    B = [0]*N
    for i in range(N):
        B[A[i]-1] = i+1
    print(*B)

solve()

=======
Suggestion 6

def main():
    N = int(input())
    A = [int(a) for a in input().split()]
    order = [0]*N
    for i in range(N):
        order[A[i]-1] = i+1
    print(*order)

=======
Suggestion 7

def main():
    N = int(input())
    A = list(map(int, input().split()))
    for i in range(1, N+1):
        print(A.index(A.index(i)+1)+1)

=======
Suggestion 8

def main():
    n = int(input())
    a = list(map(int, input().split()))
    for i in range(n):
        print(a.index(i + 1) + 1)

=======
Suggestion 9

def main():
    N = int(input())
    A = list(map(int, input().split()))
    A = [0] + A
    ans = [0] * (N+1)
    for i in range(N, 0, -1):
        ans[i] = A[i]
        for j in range(2*i, N+1, i):
            ans[i] -= ans[j]
    print(*ans[1:])

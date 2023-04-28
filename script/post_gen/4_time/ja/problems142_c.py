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

def solve():
    N = int(input())
    A = list(map(int, input().split()))
    B = [0] * N
    for i in range(N):
        B[A[i] - 1] = i + 1
    print(' '.join(map(str, B)))

=======
Suggestion 3

def main():
    n = int(input())
    a = list(map(int, input().split()))
    ans = [0] * n
    for i in range(n):
        ans[a[i] - 1] = i + 1
    print(*ans)

=======
Suggestion 4

def main():
    n = int(input())
    a = list(map(int, input().split()))
    b = [0] * n
    for i in range(n):
        b[a[i]-1] = i + 1
    print(*b)

=======
Suggestion 5

def main():
    N = int(input())
    A = list(map(int, input().split()))
    B = [0] * N
    for i in range(N):
        B[A[i]-1] = i+1
    print(*B)
main()

=======
Suggestion 6

def main():
    N = int(input())
    A = list(map(int, input().split()))
    ans = [0] * N
    for i in range(N):
        ans[A[i] - 1] = i + 1
    print(*ans)

=======
Suggestion 7

def main():
    n = int(input())
    a = list(map(int, input().split()))
    b = [0]*n
    for i in range(n):
        b[a[i]-1] = i+1
    print(' '.join(map(str, b)))

=======
Suggestion 8

def main():
    n = int(input())
    a = list(map(int, input().split()))
    b = [0 for _ in range(n)]
    for i in range(n):
        b[a[i]-1] = i+1
    print(*b)

=======
Suggestion 9

def main():
    N = int(input())
    A = list(map(int, input().split()))
    #print(N)
    #print(A)
    B = [0]*N
    for i in range(N):
        B[A[i]-1] = i+1
    #print(B)
    print(' '.join(map(str, B)))

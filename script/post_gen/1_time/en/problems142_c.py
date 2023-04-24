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
    ans = [0] * n
    for i in range(n):
        ans[a[i] - 1] = i + 1
    print(*ans)

=======
Suggestion 3

def solve():
    N = int(input())
    A = list(map(int, input().split()))
    B = [0] * N
    for i in range(N):
        B[A[i] - 1] = i + 1
    print(*B)

=======
Suggestion 4

def main():
    N = int(input())
    A = list(map(int, input().split()))
    B = [0] * N
    for i in range(N):
        B[A[i]-1] = i+1
    print(' '.join(map(str, B)))

=======
Suggestion 5

def main():
    N = int(input())
    A = list(map(int, input().split()))
    if N == 1:
        print(1)
        return

    ans = [0] * N
    for i in range(N):
        ans[A[i]-1] = i+1

    print(*ans)

=======
Suggestion 6

def main():
    N = int(input())
    A = list(map(int, input().split()))
    A = [0] + A
    index = [i for i in range(N+1)]
    index = [0] + index
    for i in range(1, N+1):
        index[A[i]] = i
    for i in range(1, N+1):
        print(index[i])

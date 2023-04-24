Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    N = int(input())
    A = list(map(int, input().split()))
    print(sum(A) - N)

=======
Suggestion 2

def main():
    N = int(input())
    A = list(map(int, input().split()))
    print(N * max(A) - sum(A))

=======
Suggestion 3

def main():
    N = int(input())
    A = list(map(int,input().split()))
    ans = 0
    for i in range(N):
        ans += (A[i]-1)
    print(ans)

=======
Suggestion 4

def main():
    N = int(input())
    A = list(map(int, input().split()))
    A.sort(reverse=True)
    ans = 0
    for i in range(N):
        ans += (A[0] - 1) % A[i]
    print(ans)

=======
Suggestion 5

def main():
    N = int(input())
    A = list(map(int, input().split()))
    A.sort()
    A = A[::-1]
    ans = 0
    for i in range(N):
        ans += A[i] * i - A[i] * (N - i - 1)
    print(ans)

=======
Suggestion 6

def main():
    N = int(input())
    A = list(map(int,input().split()))
    M = max(A)
    print(sum(A)-M)

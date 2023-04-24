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
    a = list(map(int, input().split()))
    print(sum(a) - N)

=======
Suggestion 4

def main():
    N = int(input())
    A = list(map(int,input().split()))
    A.sort()
    ans = 0
    for i in range(N):
        ans += A[i]*(N-i-1)
    print(ans)

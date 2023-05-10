Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    n = int(input())
    a = list(map(int, input().split()))
    ans = [0] * n
    for i in range(1, n):
        ans[a[i-1]-1] += 1
    for i in range(n):
        print(ans[i])

=======
Suggestion 2

def main():
    n = int(input())
    a = list(map(int,input().split()))
    b = [0]*(n+1)
    for i in range(n-1):
        b[a[i]] += 1
    for i in range(1,n+1):
        print(b[i])

=======
Suggestion 3

def main():
    N = int(input())
    A = list(map(int, input().split()))
    B = [0] * N
    for i in range(1, N):
        B[A[i-1]-1] += 1
    for i in range(N):
        print(B[i])

=======
Suggestion 4

def get_input_data():
    N = int(input())
    A = list(map(int, input().split()))
    return N, A

=======
Suggestion 5

def main():
  N = int(input())
  A = list(map(int, input().split()))
  B = [0] * N
  for i in range(1, N):
    B[A[i] - 1] += 1
  for i in range(N):
    print(B[i])

=======
Suggestion 6

def main():
    n = int(input())
    a = list(map(int, input().split()))
    ans = [0] * n
    for i in range(n - 1):
        ans[a[i] - 1] += 1
    for i in ans:
        print(i)

=======
Suggestion 7

def main():
    N = int(input())
    A = list(map(int, input().split()))

    B = [0] * N
    for i in A:
        B[i - 1] += 1

    for i in B:
        print(i)

=======
Suggestion 8

def main():
    N = int(input())
    A = list(map(int, input().split()))

    B = [0] * N
    for i in range(N-1):
        B[A[i]-1] += 1
    for i in range(N):
        print(B[i])

=======
Suggestion 9

def main():
    N = int(input())
    A = list(map(int, input().split()))
    ans = [0] * N
    for i in range(N - 1):
        ans[A[i] - 1] += 1
    for i in ans:
        print(i)

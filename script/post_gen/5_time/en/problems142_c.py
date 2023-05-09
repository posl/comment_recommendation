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
    N = int(input())
    A = list(map(int, input().split()))
    B = [0] * N
    for i in range(N):
        B[A[i] - 1] = i + 1
    print(*B)

main()

=======
Suggestion 3

def main():
    n = int(input())
    a = list(map(int, input().split()))
    b = [0] * n
    for i in range(n):
        b[a[i]-1] = i + 1
    print(' '.join(map(str, b)))

=======
Suggestion 4

def solve():
    n = int(input())
    a = list(map(int, input().split()))
    b = [0] * n
    for i in range(n):
        b[a[i] - 1] = i + 1
    print(' '.join(map(str, b)))

=======
Suggestion 5

def main():
    N = int(input())
    A = [int(i) for i in input().split()]
    B = [0] * N
    for i in range(N):
        B[A[i]-1] = i+1
    print(' '.join([str(i) for i in B]))

=======
Suggestion 6

def main():
  N = int(input())
  A = list(map(int, input().split()))
  B = [0] * N
  for i in range(N):
    B[A[i]-1] = i+1
  print(' '.join(map(str, B)))

=======
Suggestion 7

def solve():
    N = int(input())
    A = list(map(int, input().split()))
    B = [0] * N
    for i, a in enumerate(A):
        B[a-1] = str(i+1)
    print(" ".join(B))

=======
Suggestion 8

def main():
    N = int(input())
    As = list(map(int, input().split()))
    Bs = [0] * N
    for i in range(N):
        Bs[As[i]-1] = i+1
    print(*Bs)

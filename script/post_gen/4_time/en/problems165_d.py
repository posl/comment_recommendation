Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    a, b, n = map(int, input().split())
    x = min(b-1, n)
    print((a*x)//b - a*(x//b))

=======
Suggestion 2

def main():
    a, b, n = map(int, input().split())
    x = min(n, b-1)
    print((a*x)//b - a*(x//b))

=======
Suggestion 3

def main():
    a, b, n = map(int, input().split())
    x = min(b-1, n)
    print(a*x//b - a*(x//b))

=======
Suggestion 4

def main():
    A, B, N = map(int, input().split())
    if B <= N:
        x = B - 1
    else:
        x = N
    print(A*x//B - A*(x//B))

=======
Suggestion 5

def main():
    A, B, N = map(int, input().split())
    if N < B:
        print(A * N // B)
    else:
        print(A * (B - 1) // B)

=======
Suggestion 6

def main():
    # input
    A, B, N = map(int, input().split())

    # compute

    # output
    print()

=======
Suggestion 7

def solve(A, B, N):
  max = 0
  for i in range(N+1):
    tmp = A*i//B - A*(i//B)
    if tmp > max:
      max = tmp
  return max

A, B, N = map(int, input().split())
print(solve(A, B, N))

=======
Suggestion 8

def main():
    A,B,N = map(int, input().split())
    x = min(N, B-1)
    print((A*x)//B-A*(x//B))

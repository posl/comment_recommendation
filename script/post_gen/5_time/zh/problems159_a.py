Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    N, M = map(int, input().split())
    print(N*(N-1)//2 + M*(M-1)//2)

=======
Suggestion 2

def main():
  n, m = map(int, input().split())
  print((n*(n-1)//2) + (m*(m-1)//2))

=======
Suggestion 3

def main():
    n,m = map(int,input().split())
    print(n*(n-1)//2+m*(m-1)//2)

=======
Suggestion 4

def main():
    n, m = map(int, input().split())
    if n == 0 or m == 0:
        print(0)
        return

    print(n * m)

=======
Suggestion 5

def solve(n, m):
    # write code here
    return (n*(n-1)+m*(m-1))//2

=======
Suggestion 6

def main():
    N,M = map(int,input().split())
    print((N-1)*N//2 + (M-1)*M//2)

=======
Suggestion 7

def main():
    n,m = map(int, input().split())
    print((n*(n-1)+m*(m-1))//2)

=======
Suggestion 8

def solve():
    N, M = map(int, input().split())
    print(N*(N-1)//2 + M*(M-1)//2)

Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def solve():
    N, A, B = map(int, input().split())
    print(min(N*A, B))

=======
Suggestion 2

def main():
    n, a, b = map(int, input().split())
    print(min(n * a, b))

=======
Suggestion 3

def main():
    N, A, B = map(int, input().split())
    print(min(A * N, B))

=======
Suggestion 4

def main():
    n, a, b = map(int, input().split())
    if n * a < b:
        print(n * a)
    else:
        print(b)

=======
Suggestion 5

def main():
    n,a,b = map(int, input().split())
    print(min(a*n, b))

=======
Suggestion 6

def main():
    n, a, b = map(int, input().strip().split())
    print(min(a*n, b))

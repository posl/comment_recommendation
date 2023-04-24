Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    N, A, B = map(int, input().split())
    if A * N > B:
        print(B)
    else:
        print(A * N)

=======
Suggestion 2

def main():
    N, A, B = map(int, input().split())
    if A * N < B:
        print(A * N)
    else:
        print(B)

=======
Suggestion 3

def main():
    N, A, B = map(int, input().split())
    print(min(N * A, B))

=======
Suggestion 4

def main():
    N, A, B = map(int, input().split())
    print(min(A*N, B))

=======
Suggestion 5

def main():
    n, a, b = map(int, input().split())
    print(min(n*a, b))

=======
Suggestion 6

def main():
    n, a, b = map(int, input().split())
    print(min(a * n, b))

=======
Suggestion 7

def main():
    #入力
    N, A, B = map(int, input().split())
    #出力
    print(min(A * N, B))

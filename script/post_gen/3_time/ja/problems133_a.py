Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    N, A, B = map(int, input().split())
    train = N * A
    taxi = B
    if train < taxi:
        print(train)
    else:
        print(taxi)

=======
Suggestion 2

def main():
    N, A, B = map(int, input().split())
    if A * N > B:
        print(B)
    else:
        print(A * N)

=======
Suggestion 3

def main():
    n, a, b = map(int, input().split())
    taxi = n * b
    train = n * a
    if taxi <= train:
        print(taxi)
    else:
        print(train)

=======
Suggestion 4

def main():
    N, A, B = map(int, input().split())
    print(min(N * A, B))

=======
Suggestion 5

def main():
    n, a, b = map(int, input().split())
    if a*n < b:
        print(a*n)
    else:
        print(b)

=======
Suggestion 6

def main():
    N, A, B = map(int, input().split())
    print(min(A * N, B))

=======
Suggestion 7

def main():
    n, a, b = map(int, input().split())
    print(min(a*n, b))

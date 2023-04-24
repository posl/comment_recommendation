Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    K, X = map(int, input().split())
    for i in range(X - K + 1, X + K):
        print(i, end=' ')

=======
Suggestion 2

def main():
    k, x = map(int, input().split())
    print(' '.join([str(i) for i in range(x - k + 1, x + k)]))

=======
Suggestion 3

def main():
    K, X = map(int, input().split())
    print(*[i for i in range(X - K + 1, X + K)])

=======
Suggestion 4

def main():
    K, X = map(int, input().split())
    for i in range(-K + 1, K):
        print(X + i, end=' ')

main()

=======
Suggestion 5

def main():
    K, X = map(int, input().split())
    for i in range(-K+1, K):
        print(X+i, end=" ")

=======
Suggestion 6

def main():
    K, X = map(int, input().split())
    print(*range(X - K + 1, X + K))

=======
Suggestion 7

def solve():
    K, X = map(int, input().split())
    for i in range(X - K + 1, X + K):
        print(i, end=' ')
    print()

=======
Suggestion 8

def main():
    K, X = map(int, input().split())
    for i in range(-K+1, K):
        print(X+i, end=' ')
    print(X+K-1)

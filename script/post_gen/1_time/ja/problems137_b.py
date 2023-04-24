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
    K, X = map(int, input().split())
    for i in range(X - K + 1, X + K):
        print(i, end=" ")

=======
Suggestion 3

def main():
    K, X = map(int, input().split())
    for i in range(2 * K - 1):
        print(X - K + 1 + i)

=======
Suggestion 4

def main():
    K, X = map(int, input().split())
    print(" ".join(map(str, range(X - K + 1, X + K))))

=======
Suggestion 5

def main():
    K, X = map(int, input().split())
    for i in range(X - K + 1, X + K):
        print(i, end = " ")
    print()

=======
Suggestion 6

def main():
    K, X = map(int, input().split())
    for i in range(-K+1, K):
        print(X+i, end=" ")

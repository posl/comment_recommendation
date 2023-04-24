Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    k, x = map(int, input().split())
    start = x - (k - 1)
    end = x + (k - 1)
    for i in range(start, end + 1):
        print(i, end=" ")

=======
Suggestion 2

def main():
    k, x = map(int, input().split())
    start = x - k + 1
    end = x + k - 1
    for i in range(start, end + 1):
        print(i, end=' ')

=======
Suggestion 3

def main():
    k, x = map(int, input().split())
    start = x - k + 1
    end = x + k
    for i in range(start, end):
        print(i, end=" ")

=======
Suggestion 4

def main():
    k, x = map(int, input().split())
    for i in range(x-k+1, x+k):
        print(i, end=' ')

=======
Suggestion 5

def main():
    k, x = map(int, input().split())
    print(' '.join([str(i) for i in range(x - k + 1, x + k)]))

=======
Suggestion 6

def main():
    K, X = map(int, input().split())
    for i in range(X - (K - 1), X + (K - 1) + 1):
        print(i, end=" ")

=======
Suggestion 7

def main():
    k, x = map(int, input().split())
    print(*[i for i in range(x-k+1, x+k)])

=======
Suggestion 8

def main():
    k, x = map(int, input().split())
    print(' '.join(str(i) for i in range(x-k+1, x+k)))

=======
Suggestion 9

def get_inputs():
    k, x = map(int, input().split())
    return k, x

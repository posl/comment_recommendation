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
    k, x = map(int, input().split())
    for i in range(x-k+1, x+k):
        print(i, end=" ")

=======
Suggestion 4

def main():
    K, X = map(int, input().split())
    ans = [i for i in range(X - K + 1, X + K)]
    print(*ans)

=======
Suggestion 5

def main():
    # input
    K, X = map(int, input().split())

    # compute

    # output
    print(*range(X-K+1, X+K))

=======
Suggestion 6

def main():
    K, X = map(int, input().split())
    for i in range(-K+1, K):
        print(X+i)
main()

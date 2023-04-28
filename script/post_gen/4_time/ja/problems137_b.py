Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    k, x = map(int, input().split())
    for i in range(x - k + 1, x + k):
        print(i, end=" ")

=======
Suggestion 2

def main():
    k, x = map(int, input().split())
    print(*[i for i in range(x - k + 1, x + k)])

=======
Suggestion 3

def main():
    K, X = map(int, input().split())
    print(*[x for x in range(X - K + 1, X + K)])

=======
Suggestion 4

def main():
    K, X = map(int, input().split())
    if K == 1:
        print(X)
    else:
        print(" ".join(map(str, range(X - K + 1, X + K))))

=======
Suggestion 5

def main():
    K,X = map(int,input().split())
    for i in range(K):
        print(X-K+i+1,end=" ")
    for i in range(K-1):
        print(X+1+i+1,end=" ")
    print(X+K)

=======
Suggestion 6

def main():
    k, x = map(int, input().split())
    print(*range(x-k+1, x+k))

=======
Suggestion 7

def main():
    k, x = map(int, input().split())
    print(*list(range(x-k+1, x+k)))

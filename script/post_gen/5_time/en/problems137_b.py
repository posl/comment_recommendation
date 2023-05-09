Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    k, x = map(int, input().split())
    print(*[i for i in range(x - k + 1, x + k)])

=======
Suggestion 2

def main():
    K, X = map(int, input().split())
    result = []
    for i in range(X-K+1, X+K):
        result.append(i)
    print(*result)

=======
Suggestion 3

def main():
    K, X = map(int, input().split())
    print(*[i for i in range(X-K+1, X+K)])

=======
Suggestion 4

def problem137_b():
    k, x = map(int, input().split())
    print(*[i for i in range(x-k+1, x+k)])

=======
Suggestion 5

def main():
    K, X = map(int, input().split())
    print(*range(X - K + 1, X + K))

=======
Suggestion 6

def main():
    k, x = map(int, input().split())
    print(*range(x-k+1, x+k))

=======
Suggestion 7

def main():
    k, x = map(int, input().split())
    print(*[x+i for i in range(-k+1, k)])

=======
Suggestion 8

def main():
    k, x = map(int, input().split())
    print(*list(range(x-(k-1), x+k)))

=======
Suggestion 9

def f(K,X):
    result = []
    for i in range(X-K+1,X+K):
        result.append(str(i))
    return " ".join(result)

K,X = map(int,input().split())
print(f(K,X))

=======
Suggestion 10

def stones(K,X):
    result = []
    for i in range(X - K + 1, X + K):
        result.append(i)
    return result

Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    K, X = map(int, input().split())
    result = [X]
    for i in range(1, K):
        result.append(X - i)
        result.append(X + i)
    result.sort()
    print(*result)

=======
Suggestion 2

def solve(k, x):
    result = []
    for i in range(x-k+1,x+k):
        result.append(i)
    return result

=======
Suggestion 3

def main():
    k, x = map(int, input().split())
    for i in range(x-k+1, x+k):
        print(i, end=" ")
    print(x+k)

=======
Suggestion 4

def problem137_b():
    k, x = map(int, input().split())
    print(*[i for i in range(x-k+1, x+k)])

problem137_b()

=======
Suggestion 5

def main():
    K, X = map(int, input().split())
    min = X - (K - 1)
    max = X + (K - 1)
    for i in range(min, max + 1):
        print(i, end=" ")

=======
Suggestion 6

def main():
    K, X = map(int, input().split())
    if K == 1:
        print(X)
    else:
        for i in range(X - K + 1, X + K):
            print(i, end=' ')

=======
Suggestion 7

def problem137_b():
    K,X = map(int,input().split())
    for i in range(X-K+1,X+K):
        print(i,end=" ")
    print("")
problem137_b()

=======
Suggestion 8

def solve(K, X):
    return range(X - K + 1, X + K)

=======
Suggestion 9

def get_input():
    K,X = map(int, input().split())
    return K,X

=======
Suggestion 10

def main():
    k,x = map(int,input().split())
    print(" ".join(map(str,range(x-k+1,x+k))))

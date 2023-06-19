Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    k, x = map(int, input().split())
    print(' '.join(map(str, [x - k + 1, x + k - 1])))

=======
Suggestion 2

def main():
    k, x = map(int, input().split())
    max = 1000000
    min = -1000000
    if x + k > max:
        max = x + k
    if x - k < min:
        min = x - k
    for i in range(min, max+1):
        print(i, end=" ")

=======
Suggestion 3

def main():
    K,X = map(int,input().split())
    print(*[i for i in range(X-K+1,X+K)])

=======
Suggestion 4

def main():
    K, X = map(int, input().split())
    for i in range(X-K+1, X+K):
        print(i, end=' ')
    print()

=======
Suggestion 5

def main():
    k,x = map(int,input().split())
    print(" ".join([str(i) for i in range(x-k+1,x+k)]))

=======
Suggestion 6

def main():
    k, x = map(int, input().split())
    for i in range(x - k + 1, x + k):
        print(i, end=' ')

=======
Suggestion 7

def main():
    k, x = map(int, input().split())
    print(" ".join(map(str, range(x-k+1, x+k))))

=======
Suggestion 8

def main():
    K, X = map(int, input().split())
    print(' '.join(map(str, range(X - K + 1, X + K))))

=======
Suggestion 9

def main():
    k,x = map(int,input().split())
    for i in range(k):
        print(x-k+i+1,end=" ")
        print(x+i+1,end=" ")
    print()

=======
Suggestion 10

def main():
    K, X = map(int, input().split())
    left = X - K + 1
    right = X + K - 1
    for i in range(left, right+1):
        print(i, end=" ")
    print()

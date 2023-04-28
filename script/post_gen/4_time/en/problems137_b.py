Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    K, X = map(int, input().split())
    print(' '.join([str(i) for i in range(X-K+1, X+K)]))

=======
Suggestion 2

def main():
    k,x = map(int, input().split())
    min = x - k + 1
    max = x + k - 1
    for i in range(min,max+1):
        print(i, end=" ")

=======
Suggestion 3

def main():
    k, x = map(int, input().split())
    print(' '.join(map(str, range(x-k+1, x+k))))

=======
Suggestion 4

def main():
    k,x = map(int,input().split())
    for i in range(x-k+1,x+k):
        print(i,end=' ')

=======
Suggestion 5

def main():
    k, x = map(int, input().split())
    print(*range(x-k+1, x+k))

=======
Suggestion 6

def main():
    K,X = map(int,input().split())
    if K == 1:
        print(X)
    else:
        for i in range(X-(K-1),X+(K-1)+1):
            print(i,end=" ")

=======
Suggestion 7

def main():
    K, X = map(int, input().split())
    print(*range(X-K+1, X+K))

=======
Suggestion 8

def main():
    K, X = map(int, input().split())
    print(*range(X-K+1, X+K))

main()

=======
Suggestion 9

def main():
    k, x = map(int, input().split())
    print(*range(x-(k-1), x+k))

=======
Suggestion 10

def stones(K,X):
    start = X - K + 1
    end = X + K
    return [i for i in range(start, end)]

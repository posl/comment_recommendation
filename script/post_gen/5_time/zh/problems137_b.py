Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    k,x = map(int,input().split())
    if k == 1:
        print(x)
    else:
        for i in range(x-k+1,x+k):
            print(i,end=' ')

=======
Suggestion 2

def main():
    k,x = map(int, input().split())
    for i in range(x-k+1,x+k):
        print(i,end=" ")

=======
Suggestion 3

def main():
    K, X = map(int, input().split())
    start = X - K + 1
    end = X + K
    for i in range(start, end):
        print(i, end=" ")

=======
Suggestion 4

def getBlackStones(K, X):
    stones = []
    for i in range(X-K+1, X+K):
        stones.append(i)
    return stones

=======
Suggestion 5

def solve(k, x):
    # x is the position of black rock
    # k is the number of black rocks
    min = x - k + 1
    max = x + k - 1
    return range(min, max + 1)

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
    print(' '.join(map(str, [i for i in range(x-k+1, x+k)])))

=======
Suggestion 8

def main():
    k, x = map(int, input().split())
    for i in range(x-k+1, x+k):
        print(i, end=" ")
    print(x+k)

=======
Suggestion 9

def main():
    k, x = map(int, input().split())
    print(' '.join(map(str, range(x-k+1, x+k))))

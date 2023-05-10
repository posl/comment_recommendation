Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    k, x = map(int, input().split())
    print(*[i for i in range(x - k + 1, x + k)])

=======
Suggestion 2

def main():
    k, x = map(int, input().split())
    result = []
    for i in range(x-k+1, x+k):
        result.append(i)
    print(*result)

=======
Suggestion 3

def main():
    k, x = map(int, input().split())
    print(*range(x-k+1, x+k))

=======
Suggestion 4

def main():
    k,x = map(int,input().split())
    s = x - k + 1
    e = x + k - 1
    for i in range(s,e+1):
        print(i,end=" ")
    print()
main()

=======
Suggestion 5

def main():
    K, X = map(int, input().split())
    # K, X = 3, 7
    # K, X = 4, 0
    # K, X = 1, 100

    start = X - K + 1
    end = X + K
    for i in range(start, end):
        print(i, end=' ')
    print(end)

=======
Suggestion 6

def main():
    K, X = map(int, input().split())
    print(' '.join([str(i) for i in range(X-K+1, X+K)]))

=======
Suggestion 7

def main():
    k,x = map(int,input().split())
    min = x - k + 1
    max = x + k - 1
    for i in range(min,max+1):
        print(i,end=" ")

=======
Suggestion 8

def main():
    k, x = map(int, input().split())
    for i in range(x-k+1, x+k):
        print(i, end=' ')

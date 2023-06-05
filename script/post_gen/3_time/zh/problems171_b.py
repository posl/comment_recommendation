Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    n, k = map(int, input().split())
    p = list(map(int, input().split()))
    p.sort()
    print(sum(p[:k]))

=======
Suggestion 2

def main():
    n, k = map(int, input().split())
    p = list(map(int, input().split()))
    p.sort()
    sum = 0
    for i in range(k):
        sum += p[i]
    print(sum)

=======
Suggestion 3

def findMinPrice(N, K, p):
    p.sort()
    return sum(p[:K])

=======
Suggestion 4

def main():
    n,k = map(int, input().split())
    p = list(map(int, input().split()))
    p.sort()
    print(sum(p[0:k]))

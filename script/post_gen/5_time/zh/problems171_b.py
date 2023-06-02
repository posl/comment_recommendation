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

def solve():
    N, K = map(int, input().split())
    P = list(map(int, input().split()))
    P.sort()
    print(sum(P[:K]))
solve()

=======
Suggestion 3

def main():
    n, k = map(int, input().split())
    p = list(map(int, input().split()))
    p.sort()
    print(sum(p[:k]))

main()

=======
Suggestion 4

def main():
    N,K=map(int,input().split())
    p=list(map(int,input().split()))
    p.sort()
    result=0
    for i in range(K):
        result+=p[i]
    print(result)

=======
Suggestion 5

def min_price(N, K, p):
    p.sort()
    return sum(p[:K])

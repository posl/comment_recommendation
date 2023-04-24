Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    n, k = map(int, input().split())
    p = list(map(int, input().split()))
    p.sort()
    ans = 0
    for i in range(k):
        ans += p[i]
    print(ans)

main()

=======
Suggestion 2

def main():
    N, K = map(int, input().split())
    p = list(map(int, input().split()))
    p.sort()
    print(sum(p[:K]))

=======
Suggestion 3

def main():
    n, k = map(int, input().split())
    p = list(map(int, input().split()))
    p.sort()
    print(sum(p[:k]))

=======
Suggestion 4

def main():
    N, K = map(int, input().split())
    P = list(map(int, input().split()))
    P.sort()
    print(sum(P[:K]))

=======
Suggestion 5

def main():
    #Read Input
    N, K = map(int, input().split())
    p = sorted(list(map(int, input().split())))
    #Main Logic
    ans = sum(p[:K])
    #Print Output
    print(ans)

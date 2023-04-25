Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    N, K = map(int, input().split())
    C = list(map(int, input().split()))
    ans = 0
    for i in range(N-K+1):
        ans = max(ans, len(set(C[i:i+K])))

    print(ans)

=======
Suggestion 2

def main():
    n, k = map(int, input().split())
    c = list(map(int, input().split()))
    ans = 0
    for i in range(n-k+1):
        ans = max(ans, len(set(c[i:i+k])))
    print(ans)

=======
Suggestion 3

def main():
    N, K = map(int, input().split())
    c = list(map(int, input().split()))
    ans = 0
    for i in range(N-K+1):
        ans = max(ans, len(set(c[i:i+K])))
    print(ans)

=======
Suggestion 4

def main():
    n, k = map(int, input().split())
    c = list(map(int, input().split()))
    s = set(c[:k])
    ans = len(s)
    for i in range(n-k):
        s.remove(c[i])
        s.add(c[i+k])
        ans = max(ans, len(s))
    print(ans)

=======
Suggestion 5

def main():
    N, K = map(int, input().split())
    C = list(map(int, input().split()))
    print(max(len(set(C[i:i+K])) for i in range(N-K+1)))

=======
Suggestion 6

def main():
    N, K = map(int, input().split())
    C = list(map(int, input().split()))
    ans = 0
    for i in range(N-K+1):
        tmp = len(set(C[i:i+K]))
        if ans < tmp:
            ans = tmp
    print(ans)

=======
Suggestion 7

def main():
    N, K = map(int, input().split())
    candies = list(map(int, input().split()))
    colors = set()
    for i in range(K):
        colors.add(candies[i])
    max_colors = len(colors)
    for i in range(N-K):
        colors.remove(candies[i])
        colors.add(candies[i+K])
        if len(colors) > max_colors:
            max_colors = len(colors)
    print(max_colors)

=======
Suggestion 8

def main():
    N, K = map(int, input().split())
    C = list(map(int, input().split()))

    #print(N, K)
    #print(C)

    #print(len(set(C)))
    #print(len(set(C[:K])))

    #print(len(set(C[:K])))

    #print(set(C[:K]))

    #print(set(C[K:]))

    #print(set(C[K:]) - set(C[:K]))

    #print(len(set(C[:K]) | set(C[K:])))

    #print(

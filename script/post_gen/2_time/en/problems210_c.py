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
    N, K = map(int,input().split())
    C = list(map(int,input().split()))
    ans = 0
    for i in range(N-K+1):
        ans = max(ans, len(set(C[i:i+K])))
    print(ans)

main()

=======
Suggestion 4

def main():
    N, K = map(int, input().split())
    c = list(map(int, input().split()))
    max = 0
    for i in range(N-K+1):
        tmp = c[i:i+K]
        tmp = set(tmp)
        if max < len(tmp):
            max = len(tmp)
    print(max)

=======
Suggestion 5

def main():
    N, K = map(int, input().split())
    C = list(map(int, input().split()))

    #print(N, K)
    #print(C)

    ans = 0
    for i in range(N - K + 1):
        ans = max(ans, len(set(C[i:i+K])))

    print(ans)

=======
Suggestion 6

def main():
    #input
    N, K = map(int, input().split())
    Cs = list(map(int, input().split()))

    #compute
    #print(N, K, Cs)
    c = {}
    for i in range(K):
        if Cs[i] in c:
            c[Cs[i]] += 1
        else:
            c[Cs[i]] = 1
    ans = len(c)
    for i in range(K, N):
        c[Cs[i-K]] -= 1
        if c[Cs[i-K]] == 0:
            del c[Cs[i-K]]
        if Cs[i] in c:
            c[Cs[i]] += 1
        else:
            c[Cs[i]] = 1
        ans = max(ans, len(c))

    #output
    print(ans)

=======
Suggestion 7

def main():
    N, K = map(int, input().split())
    C = list(map(int, input().split()))
    #print(N, K, C)
    #print(len(C))
    max_kinds = 0
    kinds = 0
    for i in range(N):
        if not C[i] in C[i-K:i]:
            kinds += 1
        if kinds > max_kinds:
            max_kinds = kinds
        if i >= K-1:
            if not C[i-K+1] in C[i-K+2:i+1]:
                kinds -= 1
    print(max_kinds)

=======
Suggestion 8

def get_candies(N, K, candies):
    candies = candies.split()
    candies = [int(x) for x in candies]
    candies = set(candies)
    if len(candies) <= K:
        return len(candies)
    else:
        return K

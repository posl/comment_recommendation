Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    N, K = map(int, input().split())
    h = list(map(int, input().split()))
    count = 0
    for i in range(N):
        if h[i] >= K:
            count += 1
    print(count)

=======
Suggestion 2

def main():
    N, K = map(int, input().split())
    h = list(map(int, input().split()))
    ans = 0
    for i in range(N):
        if h[i] >= K:
            ans += 1
    print(ans)

=======
Suggestion 3

def main():
    n, k = map(int, input().split())
    h = list(map(int, input().split()))
    count = 0
    for i in range(n):
        if h[i] >= k:
            count += 1
    print(count)

=======
Suggestion 4

def main():
    N, K = map(int, input().split())
    H = list(map(int, input().split()))
    ans = 0
    for h in H:
        if h >= K:
            ans += 1
    print(ans)

=======
Suggestion 5

def main():
    N, K = map(int, input().split())
    h = list(map(int, input().split()))
    print(sum([1 for i in h if i >= K]))

=======
Suggestion 6

def main():
    import sys
    input = sys.stdin.readline
    N, K = map(int, input().split())
    H = list(map(int, input().split()))
    cnt = 0
    for i in range(N):
        if H[i] >= K:
            cnt += 1
    print(cnt)

=======
Suggestion 7

def main():
    N, K = list(map(int, input().split()))
    h = list(map(int, input().split()))
    print(sum([1 for i in h if i >= K]))

=======
Suggestion 8

def main():
    #N: number of friends
    #K: minimum height to ride the roller coaster
    N, K = map(int, input().split())
    #h: height of each friend
    h = list(map(int, input().split()))
    #count: number of friends who can ride the roller coaster
    count = 0
    for i in range(N):
        if h[i] >= K:
            count += 1
    print(count)

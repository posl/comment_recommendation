Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    n, k = map(int, input().split())
    h = list(map(int, input().split()))
    cnt = 0
    for i in range(n):
        if h[i] >= k:
            cnt += 1
    print(cnt)

=======
Suggestion 2

def main():
    N, K = map(int, input().split())
    h = list(map(int, input().split()))
    count = 0
    for i in range(N):
        if h[i] >= K:
            count += 1
    print(count)

=======
Suggestion 3

def main():
    N, K = map(int, input().split())
    h = list(map(int, input().split()))
    count = 0
    for i in h:
        if i >= K:
            count += 1
    print(count)

=======
Suggestion 4

def main():
    N, K = map(int, input().split())
    h = list(map(int, input().split()))
    cnt = 0
    for i in range(N):
        if h[i] >= K:
            cnt += 1
    print(cnt)

=======
Suggestion 5

def main():
    n,k = map(int,input().split())
    h = list(map(int,input().split()))
    count = 0
    for i in h:
        if i >= k:
            count += 1
    print(count)

=======
Suggestion 6

def main():
    N, K = map(int, input().split())
    h = list(map(int, input().split()))
    c = 0
    for i in range(N):
        if h[i] >= K:
            c += 1
    print(c)

=======
Suggestion 7

def roller_coaster():
    n, k = map(int, input().split())
    h = list(map(int, input().split()))
    count = 0
    for i in h:
        if i >= k:
            count += 1
    return count

=======
Suggestion 8

def main():
    n, k = map(int, input().split())
    h = list(map(int, input().split()))
    print(len([x for x in h if x >= k]))

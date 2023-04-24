Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    n, k = map(int, input().split())
    h = list(map(int, input().split()))
    count = 0
    for i in range(n):
        if h[i] >= k:
            count += 1
    print(count)

=======
Suggestion 2

def main():
    N, K = map(int, input().split())
    h = list(map(int, input().split()))
    cnt = 0
    for i in range(N):
        if h[i] >= K:
            cnt += 1
    print(cnt)

=======
Suggestion 3

def main():
    N, K = map(int, input().split())
    H = list(map(int, input().split()))
    count = 0
    for i in range(N):
        if H[i] >= K:
            count += 1
    print(count)

=======
Suggestion 4

def main():
    N, K = map(int, input().split())
    H = list(map(int, input().split()))
    H = [h for h in H if h >= K]
    print(len(H))

=======
Suggestion 5

def main():
    N, K = map(int, input().split())
    h = list(map(int, input().split()))
    print(sum([1 for i in h if i >= K]))

=======
Suggestion 6

def main():
    N, K = map(int, input().split())
    h = list(map(int, input().split()))
    print(sum(i >= K for i in h))

=======
Suggestion 7

def main():
    n, k = map(int, input().split())
    h = list(map(int, input().split()))
    print(sum(h_i >= k for h_i in h))

=======
Suggestion 8

def main():
    N,K = map(int,input().split())
    h = list(map(int,input().split()))
    counter = 0
    for i in range(N):
        if h[i]>=K:
            counter+=1
    print(counter)

=======
Suggestion 9

def main():
    #N: number of friends
    #K: height limit
    N, K = map(int, input().split())
    #h_i: height of i-th friend
    h = list(map(int, input().split()))
    count = 0
    for i in range(N):
        if h[i] >= K:
            count += 1
    print(count)

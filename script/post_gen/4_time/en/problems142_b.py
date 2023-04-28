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
    n, k = map(int, input().split())
    h = list(map(int, input().split()))
    count = 0
    for i in h:
        if i >= k:
            count += 1
    print(count)

=======
Suggestion 3

def main():
    N, K = map(int, input().split())
    h = list(map(int, input().split()))
    count = 0
    for i in range(N):
        if h[i] >= K:
            count += 1
    print(count)

=======
Suggestion 4

def main():
    N, K = map(int, input().split())
    h_list = list(map(int, input().split()))
    count = 0
    for h in h_list:
        if h >= K:
            count += 1
    print(count)

=======
Suggestion 5

def main():
    N, K = map(int, input().split())
    h = list(map(int, input().split()))
    ans = 0
    for i in range(N):
        if h[i] >= K:
            ans += 1
    print(ans)

=======
Suggestion 6

def main():
    n,k = map(int, input().split())
    h = list(map(int, input().split()))
    cnt = 0
    for i in range(n):
        if h[i] >= k:
            cnt += 1
    print(cnt)
    return

=======
Suggestion 7

def main():
    n, k = map(int, input().split())
    h = list(map(int, input().split()))
    counter = 0
    for i in range(n):
        if h[i] >= k:
            counter += 1
    print(counter)

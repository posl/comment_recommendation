Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    N = int(input())
    H = list(map(int, input().split()))
    ans = 0
    cnt = 0
    for i in range(N-1):
        if H[i] >= H[i+1]:
            cnt += 1
        else:
            ans = max(ans, cnt)
            cnt = 0
    ans = max(ans, cnt)
    print(ans)

=======
Suggestion 2

def main():
    n = int(input())
    h = list(map(int, input().split()))
    ans = 0
    cnt = 0
    for i in range(n - 1):
        if h[i] >= h[i + 1]:
            cnt += 1
        else:
            ans = max(ans, cnt)
            cnt = 0
    ans = max(ans, cnt)
    print(ans)

=======
Suggestion 3

def main():
    N = int(input())
    H = list(map(int, input().split()))
    
    count = 0
    max_count = 0
    for i in range(N-1):
        if H[i] >= H[i+1]:
            count += 1
        else:
            count = 0
        max_count = max(count, max_count)
    print(max_count)

=======
Suggestion 4

def main():
    N = int(input())
    H = list(map(int,input().split()))
    ans = 0
    for i in range(1,N):
        if H[i-1] >= H[i]:
            ans += 1
        else:
            ans = 0
    print(ans)

main()

=======
Suggestion 5

def main():
    n = int(input())
    h = [int(x) for x in input().split()]
    ans = 0
    for i in range(1, n):
        if h[i-1] >= h[i]:
            ans += 1
        else:
            ans = 0
    print(ans)
    return 0

=======
Suggestion 6

def main():
    n = int(input())
    h = list(map(int, input().split()))
    ans = 0
    for i in range(n):
        if h[i] >= h[i-1]:
            ans += 1
    print(ans)

=======
Suggestion 7

def main():
    n = int(input())
    h = list(map(int, input().split()))
    ans = 0
    for i in range(n):
        if i == 0:
            ans = 0
            continue
        if h[i] <= h[i-1]:
            ans += 1
        else:
            ans = 0
    print(ans)

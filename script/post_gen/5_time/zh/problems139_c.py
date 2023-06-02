Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    n = int(input())
    h = list(map(int, input().split()))
    cnt = 0
    tmp = 0
    for i in range(1, n):
        if h[i-1] >= h[i]:
            tmp += 1
        else:
            tmp = 0
        if cnt < tmp:
            cnt = tmp
    print(cnt)

=======
Suggestion 2

def solve():
    N = int(input())
    H = list(map(int, input().split()))
    cnt = 0
    ans = 0
    for i in range(N-1):
        if H[i] >= H[i+1]:
            cnt += 1
        else:
            ans = max(ans, cnt)
            cnt = 0
    ans = max(ans, cnt)
    print(ans)

=======
Suggestion 3

def solve():
    N = int(input())
    H = list(map(int, input().split()))

    ans = 0
    cnt = 0
    for i in range(1, N):
        if H[i-1] >= H[i]:
            cnt += 1
        else:
            ans = max(ans, cnt)
            cnt = 0
    ans = max(ans, cnt)
    print(ans)

solve()

=======
Suggestion 4

def main():
    n = int(input())
    h = list(map(int, input().split()))
    count = 0
    tmp = 0
    for i in range(1,n):
        if h[i-1] >= h[i]:
            tmp += 1
        else:
            if tmp > count:
                count = tmp
            tmp = 0
    if tmp > count:
        count = tmp
    print(count)

=======
Suggestion 5

def main():
    n = int(input())
    h = list(map(int, input().split()))
    ans = 0
    tmp = 0
    for i in range(n-1):
        if h[i] >= h[i+1]:
            tmp += 1
        else:
            if tmp > ans:
                ans = tmp
            tmp = 0
    print(ans)

=======
Suggestion 6

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
Suggestion 7

def main():
    n = int(input())
    h = list(map(int, input().split()))
    #print(n)
    #print(h)
    ans = 0
    cnt = 0
    for i in range(n-1):
        if h[i] >= h[i+1]:
            cnt += 1
        else:
            cnt = 0
        ans = max(ans, cnt)
    print(ans)

=======
Suggestion 8

def main():
    N = int(input())
    H = list(map(int, input().split()))
    ans = 0
    cnt = 0
    for i in range(N-1):
        if H[i] >= H[i+1]:
            cnt += 1
        else:
            cnt = 0
        ans = max(ans, cnt)
    print(ans)

=======
Suggestion 9

def solve():
    n = int(input())
    h = list(map(int, input().split()))
    ans = 0
    cnt = 0
    for i in range(n-1):
        if h[i] >= h[i+1]:
            cnt += 1
        else:
            ans = max(ans, cnt)
            cnt = 0
    ans = max(ans, cnt)
    print(ans)

=======
Suggestion 10

def main():
    n = int(input())
    height = list(map(int, input().split()))
    count = 0
    max_count = 0
    for i in range(1, n):
        if height[i] <= height[i - 1]:
            count += 1
        else:
            max_count = max(max_count, count)
            count = 0
    print(max(max_count, count))

Synthesizing 10/10 solutions

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
            cnt = 0
        ans = max(ans, cnt)
    print(ans)

=======
Suggestion 2

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
Suggestion 3

def main():
    n = int(input())
    h = list(map(int, input().split()))
    ans = 0
    count = 0
    for i in range(n-1):
        if h[i] >= h[i+1]:
            count += 1
        else:
            count = 0
        ans = max(ans, count)
    print(ans)

=======
Suggestion 4

def main():
    N = int(input())
    H = list(map(int, input().split()))
    cnt = 0
    max_cnt = 0
    for i in range(N-1):
        if H[i] >= H[i+1]:
            cnt += 1
            if max_cnt < cnt:
                max_cnt = cnt
        else:
            cnt = 0
    print(max_cnt)

=======
Suggestion 5

def main():
    n = int(input())
    h = list(map(int, input().split()))
    ans = 0
    for i in range(n-1):
        if h[i] >= h[i+1]:
            ans += 1
    print(ans)

=======
Suggestion 6

def main():
    n = int(input())
    h = list(map(int, input().split()))
    count = 0
    max_count = 0
    for i in range(n-1):
        if h[i] >= h[i+1]:
            count += 1
        else:
            count = 0
        if max_count < count:
            max_count = count
    print(max_count)

=======
Suggestion 7

def main():
    n = int(input())
    h = list(map(int, input().split()))
    ans = 0
    cnt = 0
    for i in range(1, n):
        if h[i - 1] >= h[i]:
            cnt += 1
        else:
            ans = max(ans, cnt)
            cnt = 0
    ans = max(ans, cnt)
    print(ans)

=======
Suggestion 8

def main():
    N = int(input())
    H = list(map(int, input().split()))
    cnt = 0
    for i in range(N - 1):
        if H[i] >= H[i + 1]:
            cnt += 1
        else:
            cnt = 0
    print(cnt)

=======
Suggestion 9

def main():
    N = int(input())
    H = list(map(int, input().split()))
    ans = 0
    count = 0
    for i in range(1, N):
        if H[i-1] >= H[i]:
            count += 1
        else:
            ans = max(ans, count)
            count = 0
    ans = max(ans, count)
    print(ans)

=======
Suggestion 10

def main():
    N = int(input())
    H = list(map(int, input().split()))
    count = 0
    for i in range(N):
        if i == 0:
            continue
        if H[i] <= H[i-1]:
            count += 1
    print(count)

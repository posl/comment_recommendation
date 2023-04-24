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
    for i in range(n-1):
        if h[i] >= h[i+1]:
            cnt += 1
            ans = max(ans, cnt)
        else:
            cnt = 0
    print(ans)

=======
Suggestion 3

def main():
    N = int(input())
    H = list(map(int, input().split()))
    ans = 0
    for i in range(N-1):
        if H[i] >= H[i+1]:
            ans += 1
        else:
            ans = 0
    print(ans)

=======
Suggestion 4

def main():
    N = int(input())
    H = list(map(int,input().split()))
    ans = 0
    count = 0
    for i in range(N-1):
        if H[i] >= H[i+1]:
            count += 1
            if count > ans:
                ans = count
        else:
            count = 0
    print(ans)

=======
Suggestion 5

def main():
    n = int(input())
    h = list(map(int, input().split()))
    cnt = 0
    max_cnt = 0
    for i in range(n-1):
        if h[i] >= h[i+1]:
            cnt += 1
        else:
            cnt = 0
        max_cnt = max(cnt, max_cnt)
    print(max_cnt)

=======
Suggestion 6

def main():
    N = int(input())
    H = list(map(int,input().split()))
    ans = 0
    for i in range(N-1):
        if H[i] >= H[i+1]:
            ans += 1
    print(ans)

=======
Suggestion 7

def main():
    N = int(input())
    H = list(map(int, input().split()))
    ans = 0
    for i in range(1, N):
        if H[i-1] >= H[i]:
            ans += 1
    print(ans)

=======
Suggestion 8

def main():
    n = int(input())
    h = list(map(int, input().split()))
    cnt = 0
    max_cnt = 0
    for i in range(1, n):
        if h[i-1] >= h[i]:
            cnt += 1
        else:
            cnt = 0
        max_cnt = max(max_cnt, cnt)
    print(max_cnt)

=======
Suggestion 9

def main():
    N = int(input())
    H = list(map(int, input().split()))
    ans = 0
    for i in range(N - 1):
        if H[i] >= H[i + 1]:
            H[i + 1] = H[i]
        else:
            ans = max(ans, H[i + 1] - H[i])
    print(ans)

Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    n = int(input())
    h = list(map(int, input().split()))

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
Suggestion 2

def main():
    n = int(input())
    h = list(map(int, input().split()))
    count = 0
    max_count = 0
    for i in range(n-1):
        if h[i] >= h[i+1]:
            count += 1
        else:
            if count > max_count:
                max_count = count
            count = 0
    if count > max_count:
        max_count = count
    print(max_count)

=======
Suggestion 3

def main():
    n = int(input())
    h = list(map(int, input().split()))
    c = 0
    m = 0
    for i in range(n-1):
        if h[i] >= h[i+1]:
            c += 1
            if c > m:
                m = c
        else:
            c = 0
    print(m)

=======
Suggestion 4

def main():
    N = int(input())
    H = list(map(int,input().split()))
    ans = 0
    cnt = 0
    for i in range(1,N):
        if H[i-1] >= H[i]:
            cnt += 1
        else:
            cnt = 0
        ans = max(ans,cnt)
    print(ans)

=======
Suggestion 5

def main():
    N = int(input())
    H = list(map(int,input().split()))
    ans = 0
    for i in range(N-1):
        if H[i] >= H[i+1]:
            ans += 1
        else:
            ans = 0
    print(ans)

=======
Suggestion 6

def main():
    n = int(input())
    h = list(map(int, input().split()))
    ans = 0
    for i in range(n):
        cnt = 0
        for j in range(i+1, n):
            if h[i] >= h[j]:
                cnt += 1
            else:
                break
        ans = max(ans, cnt)
    print(ans)

=======
Suggestion 7

def main():
    N = int(input())
    H = list(map(int,input().split()))
    count = 0
    maxcount = 0
    for i in range(N-1):
        if H[i] >= H[i+1]:
            count += 1
        else:
            count = 0
        if count > maxcount:
            maxcount = count
    print(maxcount)

=======
Suggestion 8

def main():
    n = int(input())
    h = list(map(int, input().split()))
    c = 0
    m = 0
    for i in range(1, n):
        if h[i-1] >= h[i]:
            c += 1
        else:
            c = 0
        m = max(m, c)
    print(m)

main()

=======
Suggestion 9

def main():
    n = int(input())
    h = list(map(int, input().split()))
    ans = 0
    for i in range(n):
        cnt = 0
        for j in range(i, n - 1):
            if h[j] >= h[j + 1]:
                cnt += 1
            else:
                break
        ans = max(ans, cnt)
    print(ans)

=======
Suggestion 10

def main():
    from sys import stdin
    from itertools import groupby
    _ = int(stdin.readline())
    *H, = map(int, stdin.readline().split())
    print(max(len(list(g)) for k, g in groupby(H) if k < H[0]))

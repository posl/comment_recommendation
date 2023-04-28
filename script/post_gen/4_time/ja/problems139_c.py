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
            ans = max(ans, cnt)
            cnt = 0
    ans = max(ans, cnt)
    print(ans)

=======
Suggestion 2

def solve():
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
    tmp = 0
    for i in range(n-1):
        if h[i] >= h[i+1]:
            tmp += 1
        else:
            tmp = 0
        ans = max(ans, tmp)
    print(ans)

=======
Suggestion 4

def main():
    n = int(input())
    h_list = list(map(int, input().split()))
    count = 0
    max_count = 0
    for i in range(n-1):
        if h_list[i] >= h_list[i+1]:
            count += 1
        else:
            count = 0
        max_count = max(max_count, count)
    print(max_count)

=======
Suggestion 5

def main():
    n = int(input())
    h = list(map(int, input().split()))
    count = 0
    max_count = 0
    for i in range(1, n):
        if h[i-1] >= h[i]:
            count += 1
            if count > max_count:
                max_count = count
        else:
            count = 0
    print(max_count)

=======
Suggestion 6

def solve():
    N = int(input())
    H = list(map(int, input().split()))
    count = 0
    max_count = 0
    for i in range(N - 1):
        if H[i] >= H[i + 1]:
            count += 1
        else:
            max_count = max(max_count, count)
            count = 0
    max_count = max(max_count, count)
    print(max_count)

=======
Suggestion 7

def resolve():
    N = int(input())
    H = list(map(int, input().split()))

    cnt = 0
    max_cnt = 0
    for i in range(N - 1):
        if H[i] >= H[i + 1]:
            cnt += 1
        else:
            cnt = 0
        max_cnt = max(cnt, max_cnt)

    print(max_cnt)

=======
Suggestion 8

def main():
    N = int(input())
    H = list(map(int, input().split()))
    count = 0
    for i in range(N):
        if i == 0:
            count += 1
            continue
        if H[i-1] <= H[i]:
            count += 1
    print(count)

=======
Suggestion 9

def main():
    N = int(input())
    H = list(map(int, input().split()))
    count = 0
    flag = 0
    for i in range(N-1):
        if H[i] >= H[i+1]:
            count += 1
            flag = 1
        else:
            count = 0
    print(count)

=======
Suggestion 10

def main():
    n = int(input())
    heights = [int(i) for i in input().split()]
    max_count = 0
    count = 0
    for i in range(1, n):
        if heights[i-1] >= heights[i]:
            count += 1
        else:
            count = 0
        if count > max_count:
            max_count = count
    print(max_count)

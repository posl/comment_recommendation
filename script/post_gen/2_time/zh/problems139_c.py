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
            ans = max(ans, cnt)
            cnt = 0
    ans = max(ans, cnt)
    print(ans)

=======
Suggestion 2

def solve():
    N = int(input())
    H = [int(i) for i in input().split()]
    cnt = 0
    ans = 0
    for i in range(N-1):
        if H[i] >= H[i+1]:
            cnt += 1
        else:
            cnt = 0
        ans = max(ans, cnt)
    print(ans)

solve()

=======
Suggestion 3

def main():
    N = int(input())
    H = list(map(int, input().split()))

    max_cnt = 0
    cnt = 0
    for i in range(N-1):
        if H[i] >= H[i+1]:
            cnt += 1
        else:
            max_cnt = max(max_cnt, cnt)
            cnt = 0

    max_cnt = max(max_cnt, cnt)

    print(max_cnt)

=======
Suggestion 4

def main():
    N = int(input())
    H = list(map(int, input().split()))
    max_count = 0
    count = 0
    for i in range(N - 1):
        if H[i] >= H[i + 1]:
            count += 1
            max_count = max(max_count, count)
        else:
            count = 0
    print(max_count)

=======
Suggestion 5

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
        if count > max_count:
            max_count = count
    print(max_count)

=======
Suggestion 6

def func(n, h):
    ans = 0
    cnt = 0
    for i in range(n-1):
        if h[i] >= h[i+1]:
            cnt += 1
        else:
            cnt = 0
        ans = max(ans, cnt)
    return ans

=======
Suggestion 7

def solve(n, h):
    dp = [0] * n
    dp[0] = 0
    dp[1] = 1 if h[0] >= h[1] else 0
    for i in range(2, n):
        if h[i-1] >= h[i]:
            dp[i] = dp[i-1] + 1
        else:
            dp[i] = 0
    return max(dp)

n = int(input())
h = list(map(int, input().split()))
print(solve(n, h))

=======
Suggestion 8

def main():
    n = int(input())
    h = list(map(int, input().split()))
    ans = 0
    cnt = 0
    for i in range(n - 1):
        if h[i] >= h[i + 1]:
            cnt += 1
        else:
            cnt = 0
        ans = max(ans, cnt)
    print(ans)

=======
Suggestion 9

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
Suggestion 10

def main():
    N = int(input())
    H = list(map(int, input().split()))

    # print(N)
    # print(H)

    ans = 0
    count = 0
    for i in range(N-1):
        if H[i] >= H[i+1]:
            count += 1
        else:
            ans = max(ans, count)
            count = 0
    ans = max(ans, count)
    print(ans)

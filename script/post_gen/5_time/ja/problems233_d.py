Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    n,k = map(int,input().split())
    a = list(map(int,input().split()))
    ans = 0
    right = 0
    now = 0
    for left in range(n):
        while right < n and now < k:
            now += a[right]
            right += 1
        if now == k:
            ans += 1
        if right == left:
            right += 1
        else:
            now -= a[left]
    print(ans)
main()

=======
Suggestion 2

def main():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    # print(N, K, A)
    ans = 0
    sum = 0
    right = 0
    for left in range(N):
        while right < N and sum < K:
            sum += A[right]
            right += 1
        if sum >= K:
            ans += N - right + 1
        sum -= A[left]
    print(ans)

=======
Suggestion 3

def main():
    N,K = map(int,input().split())
    A = list(map(int,input().split()))
    ans = 0
    s = 0
    d = {0:1}
    for i in range(N):
        s += A[i]
        if s - K in d:
            ans += d[s - K]
        if s in d:
            d[s] += 1
        else:
            d[s] = 1
    print(ans)

=======
Suggestion 4

def solve():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    ans = 0
    right = 0
    total = 0
    for left in range(N):
        while right < N and total < K:
            total += A[right]
            right += 1
        if total == K:
            ans += 1
        if right == left:
            right += 1
        else:
            total -= A[left]
    print(ans)

=======
Suggestion 5

def main():
    N,K = map(int,input().split())
    A = list(map(int,input().split()))
    ans = 0
    sum = 0
    r = 0
    for l in range(N):
        while r < N and sum < K:
            sum += A[r]
            r += 1
        if sum >= K:
            ans += N-r+1
        sum -= A[l]
    print(ans)
main()

=======
Suggestion 6

def main():
    N,K = map(int,input().split())
    A = list(map(int,input().split()))
    ans = 0
    s = 0
    l = 0
    r = 0
    while l < N:
        while r < N and s + A[r] < K:
            s += A[r]
            r += 1
        ans += r - l
        s -= A[l]
        l += 1
        if l == r:
            r += 1
    print(ans)

=======
Suggestion 7

def main():
    n,k = map(int,input().split())
    a = list(map(int,input().split()))
    s = [0] * (n+1)
    s[0] = 0
    for i in range(n):
        s[i+1] = s[i] + a[i]
    from collections import Counter
    c = Counter(s)
    ans = 0
    for i in range(n+1):
        ans += c[s[i]-k]
        c[s[i]] -= 1
    print(ans)

=======
Suggestion 8

def main():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    s = [0] * (N + 1)
    for i in range(N):
        s[i + 1] = s[i] + A[i]
    # print(s)
    l = 0
    r = 1
    ans = 0
    while l < N:
        # print(l, r, s[r] - s[l])
        if s[r] - s[l] == K:
            ans += 1
            l += 1
        elif s[r] - s[l] < K:
            r += 1
        else:
            l += 1
        if l == r:
            r += 1
    print(ans)

=======
Suggestion 9

def main():
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    a.insert(0, 0)
    for i in range(1, n + 1):
        a[i] += a[i - 1]
    a.insert(0, 0)
    for i in range(1, n + 1):
        a[i] += a[i - 1]
    ans = 0
    for i in range(n + 1):
        l = i
        r = n + 1
        while r - l > 1:
            m = (l + r) // 2
            if a[m] - a[i] >= k:
                r = m
            else:
                l = m
        if a[r] - a[i] == k:
            ans += 1
    print(ans)

=======
Suggestion 10

def main():
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    ans = 0
    s = 0
    l = 0
    for r in range(n):
        s += a[r]
        while s > k:
            s -= a[l]
            l += 1
        ans += r - l + 1
    print(ans)

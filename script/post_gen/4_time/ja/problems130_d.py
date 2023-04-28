Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    s = [0] * (n + 1)
    for i in range(n):
        s[i + 1] = s[i] + a[i]
    ans = 0
    r = 0
    for l in range(n):
        while r < n + 1 and s[r] - s[l] < k:
            r += 1
        ans += n - r + 1
    print(ans)

=======
Suggestion 2

def solve():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    ans = 0
    right = 0
    sum = 0
    for left in range(N):
        while right < N and sum + A[right] < K:
            sum += A[right]
            right += 1
        #print(right, sum)
        ans += right - left
        if right == left:
            right += 1
        else:
            sum -= A[left]
    print(ans)

=======
Suggestion 3

def main():
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    ans = 0
    right = 0
    sum = 0
    for left in range(n):
        while right < n and sum < k:
            sum += a[right]
            right += 1
        if sum >= k:
            ans += n - right + 1
        sum -= a[left]
    print(ans)

=======
Suggestion 4

def main():
    n, k = map(int, input().split())
    a = list(map(int, input().split()))

    ans = 0
    total = 0
    r = 0
    for l in range(n):
        while r < n and total < k:
            total += a[r]
            r += 1
        if total < k:
            break
        ans += n - r + 1
        if l == r:
            r += 1
        else:
            total -= a[l]
    print(ans)

=======
Suggestion 5

def main():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    ans = 0
    right = 0
    sum = 0
    for left in range(N):
        while right < N and sum < K:
            sum += A[right]
            right += 1
        if sum < K:
            break
        ans += N - right + 1
        sum -= A[left]
    print(ans)

=======
Suggestion 6

def main():
    N, K = map(int, input().split())
    a = list(map(int, input().split()))
    ans = 0
    s = 0
    r = 0
    for l in range(N):
        while r < N and s < K:
            s += a[r]
            r += 1
        if s >= K:
            ans += N - r + 1
        s -= a[l]
    print(ans)

=======
Suggestion 7

def main():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))

    ans = 0
    sum = 0
    right = 0
    for left in range(N):
        while right < N and sum < K:
            sum += A[right]
            right += 1
        if sum < K:
            break
        ans += N - right + 1
        sum -= A[left]
    print(ans)

main()

=======
Suggestion 8

def main():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    if min(A) > K:
        print(0)
        return
    if max(A) == K:
        print(N)
        return
    left = 0
    right = 0
    sum = 0
    cnt = 0
    while right < N:
        while right < N and sum < K:
            sum += A[right]
            right += 1
        while left <= right and sum >= K:
            sum -= A[left]
            left += 1
            cnt += N - right + 1
    print(cnt)

=======
Suggestion 9

def main():
    n,k = map(int,input().split())
    a = list(map(int,input().split()))
    sum_a = [0]
    for i in range(n):
        sum_a.append(sum_a[i]+a[i])
    ans = 0
    for i in range(n+1):
        for j in range(i+1,n+1):
            if sum_a[j] - sum_a[i] >= k:
                ans += 1
    print(ans)

=======
Suggestion 10

def main():
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    ans = 0
    # しゃくとり法
    r = 0
    s = 0
    for l in range(n):
        while r < n and s < k:
            s += a[r]
            r += 1
        if s >= k:
            ans += n - r + 1
        s -= a[l]
    print(ans)

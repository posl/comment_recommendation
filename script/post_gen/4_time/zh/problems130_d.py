Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def solve():
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    ans = 0
    sum = 0
    right = 0
    for left in range(n):
        while right < n and sum < k:
            sum += a[right]
            right += 1
        if sum < k:
            break
        ans += n - right + 1
        if right == left:
            right += 1
        else:
            sum -= a[left]
    print(ans)

=======
Suggestion 2

def solve():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))

    # しゃくとり法
    right = 0
    sum = 0
    ans = 0
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
Suggestion 3

def solve():
    N, K = map(int, input().split())
    a = list(map(int, input().split()))
    ans = 0
    s = 0
    right = 0
    for left in range(N):
        while right < N and s + a[right] < K:
            s += a[right]
            right += 1
        ans += right - left
        if right == left:
            right += 1
        else:
            s -= a[left]
    print(ans)

=======
Suggestion 4

def main():
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    ans = 0
    right = 0
    sum = 0
    for left in range(n):
        while right < n and sum + a[right] < k:
            sum += a[right]
            right += 1
        ans += right - left
        if right == left:
            right += 1
        else:
            sum -= a[left]
    print(ans)

=======
Suggestion 5

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
        if sum < k:
            break
        ans += n - right + 1
        if right == left:
            right += 1
        else:
            sum -= a[left]
    print(ans)

=======
Suggestion 6

def main():
    N,K = map(int,input().split())
    A = list(map(int,input().split()))
    ans = 0
    right = 0
    total = 0
    for left in range(N):
        while right < N and total < K:
            total += A[right]
            right += 1
        if total < K:
            break
        ans += N - right + 1
        if right == left:
            right += 1
        else:
            total -= A[left]
    print(ans)

=======
Suggestion 7

def solve():
    N, K = map(int, input().split())
    a = list(map(int, input().split()))
    ans = 0
    right = 0
    sum = 0
    for left in range(N):
        while right < N and sum + a[right] < K:
            sum += a[right]
            right += 1
        ans += right - left
        if right == left:
            right += 1
        else:
            sum -= a[left]
    print(ans)

=======
Suggestion 8

def solve():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    sum = 0
    count = 0
    right = 0
    for left in range(N):
        while right < N and sum < K:
            sum += A[right]
            right += 1
        if sum < K:
            break
        count += N - right + 1
        sum -= A[left]
    print(count)

solve()

=======
Suggestion 9

def solve(n,k,a):
    ans = 0
    sum = 0
    right = 0
    for left in range(n):
        while(right < n and sum + a[right] < k):
            sum += a[right]
            right += 1
        ans += right - left
        if left == right:
            right += 1
        else:
            sum -= a[left]
    return ans

Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    A.insert(0, 0)
    for i in range(1, N + 1):
        A[i] += A[i - 1]
    ans = 0
    for i in range(1, N + 1):
        for j in range(i, N + 1):
            if A[j] - A[i - 1] == K:
                ans += 1
    print(ans)

=======
Suggestion 2

def solve(n, k, a):
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
    return ans

=======
Suggestion 3

def main():
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    # print(n, k, a)
    ans = 0
    right = 0
    sum = 0
    for left in range(n):
        while right < n and sum < k:
            sum += a[right]
            right += 1
        if sum == k:
            ans += 1
        if right == left:
            right += 1
        else:
            sum -= a[left]
    print(ans)

=======
Suggestion 4

def solve():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    ans = 0
    right = 0
    sum = 0
    for left in range(N):
        while right < N and sum < K:
            sum += A[right]
            right += 1
        if sum == K:
            ans += 1
        if right == left:
            right += 1
        else:
            sum -= A[left]
    print(ans)

=======
Suggestion 5

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
        ans += right - left
        if left == right:
            right += 1
        else:
            sum -= A[left]
    print(ans)

=======
Suggestion 6

def solve():
    pass

=======
Suggestion 7

def main():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    sum_A = [0] * (N+1)
    for i in range(N):
        sum_A[i+1] = sum_A[i] + A[i]
    count = 0
    for i in range(N):
        for j in range(i+1, N+1):
            if sum_A[j] - sum_A[i] == K:
                count += 1
    print(count)

=======
Suggestion 8

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
        if sum == k:
            ans += 1
        if right == left:
            right += 1
        else:
            sum -= a[left]
    print(ans)

=======
Suggestion 9

def main():
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    s = [0] * (n + 1)
    for i in range(n):
        s[i + 1] = s[i] + a[i]
    ans = 0
    right = 0
    for left in range(n):
        while right < n and s[right + 1] - s[left] < k:
            right += 1
        if s[right + 1] - s[left] == k:
            ans += 1
    print(ans)

=======
Suggestion 10

def main():
    n,k = map(int,input().split())
    a = list(map(int,input().split()))
    s = [0]
    for i in range(n):
        s.append(s[i]+a[i])
    s.sort()
    ans = 0
    for i in range(n):
        ans += len([x for x in s if x == k + s[i]])
    print(ans)

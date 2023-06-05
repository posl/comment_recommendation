Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    n,k = map(int,input().split())
    a = list(map(int,input().split()))
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
Suggestion 2

def main():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    ans = 0
    right = 0
    total = 0
    for left in range(N):
        while right < N and total + A[right] < K:
            total += A[right]
            right += 1
        ans += right - left
        if left == right:
            right += 1
        else:
            total -= A[left]
    print(ans)

=======
Suggestion 3

def main():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    s = 0
    ans = 0
    right = 0
    for left in range(N):
        while right < N and s + A[right] < K:
            s += A[right]
            right += 1
        ans += right - left
        if right == left:
            right += 1
        else:
            s -= A[left]
    print(ans)

=======
Suggestion 4

def main():
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    # print(n, k, a)

    ans = 0
    right = 0
    total = 0
    for left in range(n):
        while right < n and total < k:
            total += a[right]
            right += 1
        if total < k:
            break
        ans += n - right + 1
        if left == right:
            right += 1
        else:
            total -= a[left]
    print(ans)

=======
Suggestion 5

def main():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    S = [0] * (N+1)
    for i in range(N):
        S[i+1] = S[i] + A[i]
    ans = 0
    right = 0
    for left in range(N):
        while right < N+1 and S[right] - S[left] < K:
            right += 1
        ans += N - right + 1
    print(ans)

=======
Suggestion 6

def main():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    i = 0
    j = 0
    s = 0
    ans = 0
    while(i < N):
        while(j < N and s < K):
            s += A[j]
            j += 1
        if s < K:
            break
        ans += N - j + 1
        s -= A[i]
        i += 1
    print(ans)

=======
Suggestion 7

def solve():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    ans = 0
    r = 0
    s = 0
    for l in range(N):
        while r < N and s < K:
            s += A[r]
            r += 1
        if s < K:
            break
        ans += N - r + 1
        if l == r:
            r += 1
        else:
            s -= A[l]
    print(ans)

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
        if sum < k:
            break
        ans += n - right + 1
        if right == left:
            right += 1
        else:
            sum -= a[left]
    print(ans)

=======
Suggestion 9

def solve():
    N,K=map(int,input().split())
    a=list(map(int,input().split()))
    s=[0]*(N+1)
    for i in range(N):
        s[i+1]=s[i]+a[i]
    ans=0
    right=0
    for left in range(N):
        while right<N and s[right+1]-s[left]<K:
            right+=1
        ans+=N-right
    print(ans)
solve()

=======
Suggestion 10

def solve():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    S = [0] * (N+1)
    for i in range(N):
        S[i+1] = S[i] + A[i]
    ans = 0
    right = 0
    for left in range(N):
        while right < N+1 and S[right] - S[left] < K:
            right += 1
        ans += N - right + 1
    print(ans)

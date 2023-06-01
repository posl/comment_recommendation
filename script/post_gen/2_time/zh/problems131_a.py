Synthesizing 10/10 solutions

=======
Suggestion 1

def solve(N, K, A):
    ans = 0
    sum = 0
    r = 0
    for l in range(N):
        while sum < K and r < N:
            sum += A[r]
            r += 1
        if sum < K:
            break
        ans += N - r + 1
        sum -= A[l]
    return ans

N, K = map(int, input().split())
A = list(map(int, input().split()))
print(solve(N, K, A))

=======
Suggestion 2

def solve():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    # A = [int(input()) for i in range(N)]
    ans = 0
    right = 0
    total = 0
    for left in range(N):
        while right < N and total + A[right] < K:
            total += A[right]
            right += 1
        ans += N - right
        if right == left:
            right += 1
        else:
            total -= A[left]
    print(ans)

solve()

=======
Suggestion 3

def solve():
    n,k=map(int,input().split())
    a=list(map(int,input().split()))
    s=[0]*(n+1)
    for i in range(n):
        s[i+1]=s[i]+a[i]
    ans=0
    r=0
    for l in range(n):
        while r<n and s[r+1]-s[l]<k:
            r+=1
        ans+=n-r
    print(ans)

=======
Suggestion 4

def main():
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    s = [0] * (n+1)
    for i in range(n):
        s[i+1] = s[i] + a[i]
    ans = 0
    right = 0
    for left in range(n):
        while right < n+1 and s[right] - s[left] < k:
            right += 1
        ans += n - right + 1
    print(ans)

=======
Suggestion 5

def main():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    ans = 0
    r = 0
    sum = 0
    for l in range(N):
        while r < N and sum < K:
            sum += A[r]
            r += 1
        if sum < K:
            break
        ans += N - r + 1
        if r == l:
            r += 1
        else:
            sum -= A[l]
    print(ans)
main()

=======
Suggestion 6

def main():
    N,K = map(int,input().split())
    A = list(map(int,input().split()))
    count = 0
    for i in range(N):
        sum = 0
        for j in range(i,N):
            sum += A[j]
            if sum >= K:
                count += 1
                break
    print(count)

=======
Suggestion 7

def solve():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))

    # 累積和
    S = [0] * (N + 1)
    for i in range(N):
        S[i + 1] = S[i] + A[i]

    # しゃくとり法
    res = 0
    r = 0
    for l in range(N):
        while r < N + 1 and S[r] - S[l] < K:
            r += 1
        res += N - r + 1
    print(res)

solve()

=======
Suggestion 8

def solve():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    ans = 0
    total = 0
    right = 0
    for left in range(N):
        while right < N and total + A[right] < K:
            total += A[right]
            right += 1
        ans += right - left
        if right == left:
            right += 1
        else:
            total -= A[left]
    print(ans)

solve()

=======
Suggestion 9

def problems130_d(N, K, A):
    count = 0
    start = 0
    end = 0
    sum = A[0]
    while start < N and end < N:
        if sum < K:
            end += 1
            if end < N:
                sum += A[end]
        else:
            count += N - end
            sum -= A[start]
            start += 1
    return count

=======
Suggestion 10

def main():
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    ans = 0
    right = 0
    total = 0
    for left in range(n):
        while (right < n) and (total < k):
            total += a[right]
            right += 1
        if total < k:
            break
        ans += n - right + 1
        total -= a[left]
    print(ans)

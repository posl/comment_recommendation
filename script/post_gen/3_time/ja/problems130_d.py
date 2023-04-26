Synthesizing 10/10 solutions

=======
Suggestion 1

def readinput():
    n,k=list(map(int,input().split()))
    a=list(map(int,input().split()))
    return n,k,a

=======
Suggestion 2

def solve():
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
        if sum < K:
            break
        ans += N - right + 1
        if left == right:
            right += 1
        else:
            sum -= A[left]
    print(ans)
solve()

=======
Suggestion 4

def main():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))

    sumA = [0] * (N + 1)
    for i in range(N):
        sumA[i + 1] = sumA[i] + A[i]

    r = 0
    ans = 0
    for l in range(N):
        while r < N and sumA[r + 1] - sumA[l] < K:
            r += 1
        ans += N - r

    print(ans)

=======
Suggestion 5

def main():
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    s = [0]
    for i in range(n):
        s.append(s[-1] + a[i])

    ans = 0
    r = 0
    for l in range(n+1):
        while r < n+1 and s[r] - s[l] < k:
            r += 1
        ans += n - r + 1

    print(ans)

=======
Suggestion 6

def main():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    cnt = 0
    for i in range(N):
        sum = 0
        for j in range(i, N):
            sum += A[j]
            if sum >= K:
                cnt += 1
    print(cnt)

=======
Suggestion 7

def main():
    # input
    N, K = map(int, input().split())
    A = list(map(int, input().split()))

    # compute
    cnt = 0
    for i in range(N):
        for j in range(i, N):
            if sum(A[i:j+1]) >= K:
                cnt += 1

    # output
    print(cnt)

=======
Suggestion 8

def main():
    N, K = map(int, input().split())
    a = list(map(int, input().split()))
    #print(N, K, a)
    ans = 0
    right = 0
    total = 0
    for left in range(N):
        while right < N and total < K:
            total += a[right]
            right += 1
        if total >= K:
            ans += N - right + 1
        total -= a[left]
    print(ans)
main()

=======
Suggestion 9

def main():
    N,K = map(int,input().split())
    a = list(map(int,input().split()))
    s = 0
    left = 0
    right = 0
    ans = 0
    while right < N:
        while s < K:
            if right == N:
                break
            s += a[right]
            right += 1
        while s >= K:
            ans += N - right + 1
            s -= a[left]
            left += 1
    print(ans)

=======
Suggestion 10

def solve():
    N, K = map(int,input().split())
    A = list(map(int,input().split()))

    # Aの累積和を求める
    S = [0] * (N + 1)
    for i in range(N):
        S[i + 1] = S[i] + A[i]

    # 尺取り法で解く
    ans = 0
    r = 0
    for l in range(N):
        while r < N and S[r + 1] - S[l] < K:
            r += 1
        ans += N - r

    print(ans)

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
    d = {}
    for i in range(n + 1):
        if s[i] - k in d:
            ans += d[s[i] - k]
        if s[i] in d:
            d[s[i]] += 1
        else:
            d[s[i]] = 1
    print(ans)

=======
Suggestion 2

def main():
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    s = [0] * (n + 1)
    for i in range(n):
        s[i + 1] = s[i] + a[i]
    from collections import defaultdict
    d = defaultdict(int)
    ans = 0
    for i in range(n + 1):
        ans += d[s[i]]
        d[s[i] + k] += 1
    print(ans)

=======
Suggestion 3

def main():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    S = [0] * (N + 1)
    for i in range(N):
        S[i + 1] = S[i] + A[i]
    from collections import defaultdict
    d = defaultdict(int)
    ans = 0
    for i in range(N + 1):
        ans += d[S[i]]
        d[S[i] + K] += 1
    print(ans)

=======
Suggestion 4

def main():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    S = [0] * (N + 1)
    for i in range(N):
        S[i + 1] = S[i] + A[i]
    r = 0
    ans = 0
    for l in range(N):
        while r < N and S[r + 1] - S[l] < K:
            r += 1
        if S[r + 1] - S[l] == K:
            ans += 1
    print(ans)

=======
Suggestion 5

def main():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    A = [0] + A
    for i in range(N):
        A[i+1] += A[i]
    ans = 0
    for i in range(N+1):
        for j in range(i+1, N+1):
            if A[j] - A[i] == K:
                ans += 1
    print(ans)

=======
Suggestion 6

def main():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    sumA = [0]
    for i in range(N):
        sumA.append(sumA[i] + A[i])
    #print(sumA)
    results = 0
    for i in range(N+1):
        for j in range(i+1, N+1):
            if sumA[j] - sumA[i] == K:
                results += 1
    print(results)

=======
Suggestion 7

def main():
    n,k = map(int,input().split())
    a = list(map(int,input().split()))
    sum_a = [0]*(n+1)
    for i in range(n):
        sum_a[i+1] = sum_a[i]+a[i]
    ans = 0
    for i in range(n):
        for j in range(i,n):
            if sum_a[j+1]-sum_a[i] == k:
                ans += 1
    print(ans)

=======
Suggestion 8

def main():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    total = 0
    left = 0
    right = 0
    while left < N:
        while right < N:
            total += A[right]
            if total >= K:
                break
            right += 1
        if total < K:
            break
        if total == K:
            print("left: {}, right: {}".format(left, right))
        total -= A[left]
        left += 1
        right += 1
    print("total: {}".format(total))

=======
Suggestion 9

def main():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))

    # 累積和を求める
    S = [0]
    for i in range(N):
        S.append(S[i] + A[i])

    # 累積和を用いて、条件を満たす区間の数を求める
    cnt = 0
    for i in range(N):
        for j in range(i+1, N+1):
            if S[j] - S[i] == K:
                cnt += 1

    print(cnt)

=======
Suggestion 10

def main():
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    # a = [int(input()) for i in range(n)]
    # a = [list(map(int, input().split())) for i in range(n)]
    # a = [input() for i in range(n)]
    # a = [list(input()) for i in range(n)]
    # a = [str(input()) for i in range(n)]
    # a = [list(map(str, input().split())) for i in range(n)]
    # a = [list(input().split()) for i in range(n)]
    # a = [list(map(int, input().split())) for i in range(n)]
    # a = [list(map(str, input().split())) for i in range(n)]
    # a = [int(input()) for i in range(n)]
    # a = [list(map(int, input().split())) for i in range(n)]
    # a = [input() for i in range(n)]
    # a = [list(input()) for i in range(n)]
    # a = [str(input()) for i in range(n)]
    # a = [list(map(str, input().split())) for i in range(n)]
    # a = [list(input().split()) for i in range(n)]
    # a = [list(map(int, input().split())) for i in range(n)]
    # a = [list(map(str, input().split())) for i in range(n)]
    # a = [int(input()) for i in range(n)]
    # a = [list(map(int, input().split())) for i in range(n)]
    # a = [input() for i in range(n)]
    # a = [list(input()) for i in range(n)]
    # a = [str(input()) for i in range(n)]
    # a = [list(map(str, input().split())) for i in range(n)]
    # a = [list(input().split()) for i in range(n)]
    # a = [list(map(int, input().split())) for i in range(n)]
    # a = [list(map(str, input().split())) for i in range(n)]

    # a = [int(input()) for i in range(n)]
    # a = [list(map(int, input().split())) for i in range(n)]

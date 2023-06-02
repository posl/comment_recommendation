Synthesizing 10/10 solutions

=======
Suggestion 1

def solve():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    sum = 0
    cnt = 0
    right = 0
    for left in range(N):
        while right < N and sum < K:
            sum += A[right]
            right += 1
        if sum == K:
            cnt += 1
        if left == right:
            right += 1
        else:
            sum -= A[left]
    print(cnt)

=======
Suggestion 2

def main():
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    cnt = 0
    for i in range(n):
        tmp = 0
        for j in range(i, n):
            tmp += a[j]
            if tmp == k:
                cnt += 1
    print(cnt)

=======
Suggestion 3

def solve():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    S = [0] * (N + 1)
    for i in range(N):
        S[i + 1] = S[i] + A[i]
    from collections import defaultdict
    d = defaultdict(int)
    ans = 0
    for i in range(N + 1):
        ans += d[S[i] - K]
        d[S[i]] += 1
    return ans

print(solve())

=======
Suggestion 4

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
        if s == K:
            ans += 1
        if r == l:
            r += 1
        else:
            s -= A[l]
    print(ans)

=======
Suggestion 5

def main():
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    s = [0]
    for i in range(n):
        s.append(s[i] + a[i])
    #print(s)
    #print(len(s))
    cnt = 0
    for i in range(n+1):
        for j in range(i+1, n+1):
            if s[j] - s[i] == k:
                cnt += 1
    print(cnt)

=======
Suggestion 6

def solve():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    # print(N, K, A)
    # print(A[0])
    # print(A[0] + A[1])
    # print(A[0] + A[1] + A[2])
    # print(A[0] + A[1] + A[2] + A[3])
    # print(A[0] + A[1] + A[2] + A[3] + A[4])
    # print(A[0] + A[1] + A[2] + A[3] + A[4] + A[5])

    # print(A[1])
    # print(A[1] + A[2])
    # print(A[1] + A[2] + A[3])
    # print(A[1] + A[2] + A[3] + A[4])
    # print(A[1] + A[2] + A[3] + A[4] + A[5])
    # print(A[2])
    # print(A[2] + A[3])
    # print(A[2] + A[3] + A[4])
    # print(A[2] + A[3] + A[4] + A[5])
    # print(A[3])
    # print(A[3] + A[4])
    # print(A[3] + A[4] + A[5])
    # print(A[4])
    # print(A[4] + A[5])
    # print(A[5])
    # print(A[0] - K)
    # print(A[0] + A[1] - K)
    # print(A[0] + A[1] + A[2] - K)
    # print(A[0] + A[1] + A[2] + A[3] - K)
    # print(A[0] + A[1] + A[2] + A[3] + A[4] - K)
    # print(A[0] + A[1] + A[2] + A[3] + A[4] + A[5] - K)
    # print(A[1] - K

=======
Suggestion 7

def main():
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    s = [0] * (n + 1)
    for i in range(n):
        s[i + 1] = s[i] + a[i]
    ans = 0
    j = 0
    for i in range(n):
        while j <= n and s[j] - s[i] < k:
            j += 1
        if s[j] - s[i] == k:
            ans += 1
    print(ans)

=======
Suggestion 8

def main():
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    s = 0
    l = 0
    ans = 0
    for r in range(n):
        s += a[r]
        while s > k:
            s -= a[l]
            l += 1
        ans += r - l + 1
    print(ans)

=======
Suggestion 9

def main():
    n,k = map(int,input().split())
    a = list(map(int,input().split()))
    left = 0
    right = 0
    s = a[0]
    ans = 0
    while left < n:
        if s == k:
            ans += 1
            s -= a[left]
            left += 1
            if right < left:
                right = left
                s = a[left]
        elif s < k:
            right += 1
            if right < n:
                s += a[right]
            else:
                break
        else:
            s -= a[left]
            left += 1
            if right < left:
                right = left
                s = a[left]
    print(ans)

=======
Suggestion 10

def get_input():
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    return n, k, a

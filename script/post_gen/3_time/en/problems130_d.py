Synthesizing 10/10 solutions

=======
Suggestion 1

def solve():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    ans = 0
    s = 0
    l = 0
    for r in range(N):
        s += A[r]
        while s >= K:
            ans += N - r
            s -= A[l]
            l += 1
    print(ans)

=======
Suggestion 2

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

=======
Suggestion 3

def main():
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    s = [0]
    for i in range(n):
        s.append(s[-1] + a[i])
    ans = 0
    for i in range(n):
        for j in range(i+1, n+1):
            if s[j] - s[i] >= k:
                ans += 1
    print(ans)

=======
Suggestion 4

def main():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    ans = 0
    sum = 0
    l = 0
    for r in range(N):
        sum += A[r]
        while sum >= K:
            ans += N - r
            sum -= A[l]
            l += 1
    print(ans)

=======
Suggestion 5

def main():
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    s = 0
    cnt = 0
    l = 0
    for r in range(n):
        s += a[r]
        while s >= k:
            cnt += n-r
            s -= a[l]
            l += 1
    print(cnt)

=======
Suggestion 6

def main():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    sum = 0
    count = 0
    i = 0
    j = 0
    while i < N:
        while j < N:
            sum += A[j]
            if sum >= K:
                count += N - j
                break
            j += 1
        sum -= A[i]
        i += 1
    print(count)
main()

=======
Suggestion 7

def main():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))

    result = 0
    right = 0
    total = 0
    for left in range(N):
        while right < N and total < K:
            total += A[right]
            right += 1
        if total < K:
            break
        result += N - right + 1
        total -= A[left]

    print(result)

=======
Suggestion 8

def main():
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    s = [0]
    for x in a:
        s.append(s[-1] + x)
    s.append(0)
    # print(s)
    ans = 0
    for i in range(n+1):
        for j in range(i+1, n+2):
            if s[j] - s[i] >= k:
                # print(i, j, s[j] - s[i])
                ans += 1
    print(ans)

=======
Suggestion 9

def solve(N, K, A):
    #print(N, K, A)
    s = 0
    l = 0
    r = 0
    ans = 0
    while r < N:
        s += A[r]
        while s >= K:
            ans += N-r
            s -= A[l]
            l += 1
        r += 1
    return ans

=======
Suggestion 10

def main():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    #print(A)
    #print(N)
    #print(K)
    #print(len(A))

    s = 0
    r = 0
    ans = 0
    for l in range(N):
        while r < N and s < K:
            s += A[r]
            r += 1
        if s < K:
            break
        ans += N-r+1
        if l == r:
            r += 1
        else:
            s -= A[l]
    print(ans)

Synthesizing 10/10 solutions

=======
Suggestion 1

def problems130_d():
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    s = [0]
    for i in range(n):
        s.append(s[i] + a[i])
    ans = 0
    l = 0
    r = 1
    while l <= n:
        if s[r] - s[l] >= k:
            ans += n - r + 1
            l += 1
        else:
            if r < n:
                r += 1
            else:
                l += 1
    print(ans)
problems130_d()

=======
Suggestion 2

def solve():
    N, K = map(int, input().split())
    a = list(map(int, input().split()))
    s = 0
    r = 0
    ans = 0
    for l in range(N):
        while r < N and s < K:
            s += a[r]
            r += 1
        if s < K:
            break
        ans += N - r + 1
        s -= a[l]
    print(ans)

=======
Suggestion 3

def solve(n,k,a):
    ans = 0
    s = 0
    r = 0
    for l in range(n):
        while r < n and s < k:
            s += a[r]
            r += 1
        if s >= k:
            ans += n - r + 1
        s -= a[l]
    return ans

=======
Suggestion 4

def problem():
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    ans = 0
    s = 0
    r = 0
    for l in range(n):
        while r < n and s < k:
            s += a[r]
            r += 1
        if s >= k:
            ans += n-r+1
        s -= a[l]
    print(ans)

problem()

=======
Suggestion 5

def main():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    sum_a = [0]
    for i in range(N):
        sum_a.append(sum_a[i] + A[i])
    ans = 0
    for i in range(N):
        for j in range(i+1, N+1):
            if sum_a[j] - sum_a[i] >= K:
                ans += 1
    print(ans)

=======
Suggestion 6

def main():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    s = 0
    cnt = 0
    ans = 0
    for i in range(N):
        while s < K:
            if cnt == N:
                break
            s += A[cnt]
            cnt += 1
        if s < K:
            break
        ans += N-cnt+1
        s -= A[i]
    print(ans)
main()

=======
Suggestion 7

def main():
    n,k = map(int,input().split())
    a = list(map(int,input().split()))
    result = 0
    s = 0
    r = 0
    for l in range(n):
        while r < n and s < k:
            s += a[r]
            r += 1
        if s >= k:
            result += n - r + 1
        s -= a[l]
    print(result)

=======
Suggestion 8

def problem():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))

    count = 0
    for i in range(N):
        total = 0
        for j in range(i, N):
            total += A[j]
            if total >= K:
                count += N - j
                break
    print(count)

=======
Suggestion 9

def get_input():
    N, K = map(int, input().split())
    a = list(map(int, input().split()))
    return N, K, a

=======
Suggestion 10

def solve():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))

    acc = 0
    accs = [0]
    for i in range(N):
        acc += A[i]
        accs.append(acc)

    ans = 0
    for i in range(N+1):
        for j in range(i+1, N+1):
            if accs[j] - accs[i] >= K:
                ans += 1
    print(ans)

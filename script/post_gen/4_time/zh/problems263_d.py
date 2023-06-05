Synthesizing 10/10 solutions

=======
Suggestion 1

def solve():
    N, L, R = map(int, input().split())
    A = list(map(int, input().split()))
    ans = 0
    for i in range(N):
        ans += A[i]
    for i in range(1, N):
        A[i] = min(A[i], A[i - 1] + L)
    for i in range(N - 2, -1, -1):
        A[i] = min(A[i], A[i + 1] + R)
    for i in range(N):
        ans += A[i] - A[i]
    print(ans)

=======
Suggestion 2

def main():
    n,l,r = map(int, input().split())
    a = list(map(int, input().split()))
    if l > r:
        l,r = r,l
    if l >= 0:
        ans = sum(a) + l * n
    elif r <= 0:
        ans = sum(a) + r * n
    else:
        ans = sum(a)
        m = 0
        for i in range(n):
            if a[i] < 0:
                if l + a[i] < 0:
                    m += (l + a[i])
                    a[i] = 0
                else:
                    a[i] += l
        if m < 0:
            for i in range(n):
                if a[i] > 0:
                    if r + a[i] > 0:
                        m += (r + a[i])
                        a[i] = 0
                    else:
                        a[i] += r
                if m >= 0:
                    break
        ans += m
    print(ans)

=======
Suggestion 3

def main():
    n,l,r = map(int, input().split())
    a = list(map(int, input().split()))
    for i in range(n):
        a[i] = a[i] - l
    # print(a)
    # print(sum(a))
    dp = [[0 for i in range(2)] for j in range(n+1)]
    for i in range(n):
        dp[i+1][0] = max(dp[i][0], dp[i][1])
        dp[i+1][1] = max(dp[i][0] + a[i], dp[i][1] + a[i])
    print(max(dp[n][0], dp[n][1]) + n * r)
    return

=======
Suggestion 4

def main():
    n,l,r = map(int,input().split())
    a = list(map(int,input().split()))
    a.sort()
    s = sum(a[:l])
    for i in range(l,n):
        s += min(a[i],a[l-1])
    print(s)

=======
Suggestion 5

def main():
    n,l,r = map(int,input().split())
    a = list(map(int,input().split()))
    sum = 0
    for i in range(n):
        if a[i] < 0:
            sum += a[i]*(l+r)
        else:
            sum += a[i]*(l-r)
    print(sum)

=======
Suggestion 6

def main():
    n,l,r=map(int,input().split())
    a=list(map(int,input().split()))
    print(min(sum(a),sum(a[:l])+l*min(a[l:]),sum(a[:r])+r*min(a[r:])))

=======
Suggestion 7

def solve(a, l, r):
    n = len(a)
    if n == 1:
        return a[0]
    elif n == 2:
        return min(a[0] * l + a[1] * r, (a[0] + a[1]) * l)
    else:
        return min(a[0] * l + a[1] * r + sum(a[2:]) * r, (a[0] + a[1]) * l + sum(a[2:]) * r, a[0] * l + (a[1] + sum(a[2:])) * r, (a[0] + a[1]) * l + (sum(a[2:])) * r, a[0] * l + a[1] * r + sum(a[2:]) * l, (a[0] + a[1]) * l + sum(a[2:]) * l, a[0] * l + (a[1] + sum(a[2:])) * l, (a[0] + a[1]) * l + (sum(a[2:])) * l)


n, l, r = map(int, input().split())
a = list(map(int, input().split()))
print(solve(a, l, r))

=======
Suggestion 8

def solve():
    N, L, R = map(int, input().split())
    A = list(map(int, input().split()))
    # print(N, L, R)
    # print(A)
    A.sort()
    # print(A)
    ans = 0
    for i in range(N):
        if A[i] < 0:
            if L > 0:
                L -= 1
                ans += -A[i]
            elif R > 0:
                R -= 1
                ans += -A[i]
            else:
                ans += A[i]
        else:
            if R > 0:
                R -= 1
                ans += A[i]
            elif L > 0:
                L -= 1
                ans += A[i]
            else:
                ans += -A[i]
    print(ans)

=======
Suggestion 9

def main():
    n, l, r = map(int, input().split())
    a = list(map(int, input().split()))
    a.sort()
    ans = 0
    for i in range(n):
        if a[i] < 0:
            if l > 0:
                ans += l
                l = 0
            else:
                ans += a[i]
        elif a[i] > 0:
            if r > 0:
                ans += r
                r = 0
            else:
                ans += a[i]
        else:
            ans += l + r
            l = r = 0
    print(ans)

=======
Suggestion 10

def main():
    n, l, r = map(int, input().split())
    a = list(map(int, input().split()))
    a.sort()
    ans = 0
    for i in range(n):
        if a[i] < 0:
            if l + r < 0:
                ans += l + r
                l = 0
                r = 0
            else:
                ans += a[i]
        elif l + r < a[i]:
            ans += l + r
            l = 0
            r = 0
        else:
            ans += a[i]
            if l > r:
                l -= a[i]
            else:
                r -= a[i]
    print(ans)

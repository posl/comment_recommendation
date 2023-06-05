Synthesizing 9/10 solutions

=======
Suggestion 1

def main():
    n, l, r = map(int, input().split())
    a = list(map(int, input().split()))
    a.sort()
    a.reverse()
    sum = 0
    for i in range(n):
        if i < l:
            sum += a[i]
        else:
            sum += a[l-1]
    print(sum)

=======
Suggestion 2

def main():
    n, l, r = map(int, input().split())
    a = list(map(int, input().split()))
    a.sort()
    #print(a)
    if l == 0 and r == 0:
        print(sum(a))
        return
    elif l == 0 and r != 0:
        print(sum(a) + r*len(a))
        return
    elif l != 0 and r == 0:
        print(sum(a) + l*len(a))
        return
    else:
        sum1 = sum(a) + l*len(a)
        sum2 = sum(a) + r*len(a)
        #print(sum1, sum2)
        if sum1 < sum2:
            print(sum1)
            return
        else:
            print(sum2)
            return

=======
Suggestion 3

def main():
    n, l, r = map(int, input().split())
    a = list(map(int, input().split()))
    a.sort()
    a.reverse()
    if l == r == 0:
        print(sum(a))
        return
    if l > r:
        l, r = r, l
    if a[0] >= 0:
        print(sum(a) + l * (n - 1))
        return
    if a[-1] <= 0:
        print(sum(a) + r * (n - 1))
        return
    i = 0
    while i < n and a[i] > 0:
        i += 1
    if i == n:
        print(sum(a) + l * (n - 1))
        return
    j = i
    while j < n and a[j] == 0:
        j += 1
    if j == n:
        print(sum(a) + l * (n - 1))
        return
    k = j
    while k < n and a[k] < 0:
        k += 1
    if k == n:
        print(sum(a) + r * (n - 1))
        return
    ans = 0
    for x in range(i):
        ans += a[x] * (l + r)
    for x in range(i, j):
        ans += a[x] * (l + r)
    for x in range(j, k):
        ans += a[x] * (l + r)
    for x in range(k, n):
        ans += a[x] * (l + r)
    print(ans)

=======
Suggestion 4

def main():
    n, l, r = map(int, input().split())
    a = list(map(int, input().split()))
    for i in range(n):
        a[i] = a[i] + l
    a.sort(reverse=True)
    ans = 0
    for i in range(n):
        if i < r:
            ans += a[i]
        else:
            ans += min(a[i], a[r - 1])
    print(ans)

=======
Suggestion 5

def main():
    N,L,R = map(int,input().split())
    A = list(map(int,input().split()))
    min = 0
    for i in range(N):
        if A[i] > 0:
            min += A[i]
        else:
            min -= A[i]
    print(min)
    min = 0
    for i in range(N):
        if A[i] < 0:
            min += A[i]
        else:
            min += A[i]
    print(min)

=======
Suggestion 6

def main():
    N, L, R = map(int, input().split())
    A = list(map(int, input().split()))

    #print(N, L, R)
    #print(A)
    sum = 0
    for i in range(N):
        sum += A[i]

    sum_min = sum
    for i in range(N):
        for j in range(N):
            sum_tmp = sum
            for k in range(i):
                sum_tmp -= L
            for k in range(N-j, N):
                sum_tmp -= R
            if i < j:
                sum_tmp += (j-i) * L
            elif i > j:
                sum_tmp += (i-j) * R
            if sum_tmp < sum_min:
                sum_min = sum_tmp

    print(sum_min)

=======
Suggestion 7

def solve(N, L, R, A):
    # L, R, A = map(int, input().split())
    # A = list(map(int, input().split()))
    # N = len(A)

    # dp[i] = (A_i, A_{i+1}, ... A_N)での最小コスト
    dp = [float('inf')] * (N + 1)
    dp[0] = 0

    for i in range(N):
        dp[i + 1] = min(dp[i + 1], dp[i] + A[i] * L)
        dp[i + 1] = min(dp[i + 1], dp[i] + R)
        if i + 1 < N:
            dp[i + 2] = min(dp[i + 2], dp[i] + A[i] * L + R)
        if i + 2 < N:
            dp[i + 3] = min(dp[i + 3], dp[i] + A[i] * L + R * 2)
        if i + 3 < N:
            dp[i + 4] = min(dp[i + 4], dp[i] + A[i] * L + R * 3)
        if i + 4 < N:
            dp[i + 5] = min(dp[i + 5], dp[i] + A[i] * L + R * 4)
        if i + 5 < N:
            dp[i + 6] = min(dp[i + 6], dp[i] + A[i] * L + R * 5)
        if i + 6 < N:
            dp[i + 7] = min(dp[i + 7], dp[i] + A[i] * L + R * 6)
        if i + 7 < N:
            dp[i + 8] = min(dp[i + 8], dp[i] + A[i] * L + R * 7)
        if i + 8 < N:
            dp[i + 9] = min(dp[i + 9], dp[i] + A[i] * L + R * 8)
        if i + 9 < N:
            dp[i + 10] = min(dp[i + 10], dp[i] + A[i] * L + R * 9)
        if i +

=======
Suggestion 8

def solve():
    N, L, R = map(int, input().split())
    A = list(map(int, input().split()))
    #print(N, L, R)
    #print(A)
    if L >= 0:
        print(sum(A) + N * L)
    elif R <= 0:
        print(sum(A) + N * R)
    else:
        sumA = sum(A)
        minA = min(A)
        maxA = max(A)
        if sumA < 0:
            print(sumA + N * R)
        elif sumA > 0:
            print(sumA + N * L)
        else:
            if L < 0:
                print(sumA + N * (L - minA))
            else:
                print(sumA + N * (R - maxA))

solve()

=======
Suggestion 9

def main():
    N,L,R = map(int,input().split())
    A = list(map(int,input().split()))
    for i in range(N):
        if A[i] < 0:
            A[i] = -1*A[i]
    if L > R:
        A.sort(reverse=True)
        A[L-1:N] = [R]*(N-L+1)
    else:
        A.sort()
        A[0:L] = [L]*(L)
    print(sum(A))

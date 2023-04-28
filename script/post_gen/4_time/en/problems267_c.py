Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    s = [0]
    for i in range(n):
        s.append(s[-1] + a[i])
    t = [0]
    for i in range(n):
        t.append(t[-1] + i * a[i])
    ans = 0
    for i in range(n - m + 1):
        ans = max(ans, t[i + m] - t[i] - s[i] * m)
    print(ans)

=======
Suggestion 2

def main():
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    sum_a = [0]
    for i in range(n):
        sum_a.append(sum_a[i] + a[i])
    max_sum = -float('inf')
    for i in range(n-m+1):
        max_sum = max(max_sum, sum_a[i+m] - sum_a[i])
    print(max_sum)

=======
Suggestion 3

def solve():
    N,M = map(int,input().split())
    A = list(map(int,input().split()))
    B = [0]*(N+1)
    for i in range(N):
        B[i+1] = B[i] + A[i]
    C = [0]*(N+1)
    for i in range(N):
        C[i+1] = C[i] + i*A[i]
    D = [0]*(N+1)
    for i in range(N):
        D[i+1] = D[i] + A[i]
    for i in range(N):
        D[i+1] = max(D[i+1],D[i])
    ans = 0
    for i in range(N-M+1):
        ans = max(ans,C[i+M]-C[i]-B[i]*M+D[i])
    print(ans)
solve()

=======
Suggestion 4

def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))

    B = [0] * N
    for i in range(N):
        B[i] = A[i] + B[i-1]

    ans = 0
    for i in range(M-1, N):
        ans = max(ans, B[i] - B[i-M])

    print(ans)

=======
Suggestion 5

def main():
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    s = sum(a[:m])
    ans = s
    for i in range(1, n - m + 1):
        s += a[m + i - 1] - a[i - 1]
        ans = max(ans, s)
    print(ans)

=======
Suggestion 6

def max_subarray(arr):
    max_so_far = 0
    max_ending_here = 0
    for i in range(len(arr)):
        max_ending_here = max_ending_here + arr[i]
        if max_ending_here < 0:
            max_ending_here = 0
        if max_ending_here > max_so_far:
            max_so_far = max_ending_here
    return max_so_far

=======
Suggestion 7

def solve():
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    ans = 0
    for i in range(n):
        for j in range(i, n):
            b = a[i:j+1]
            if len(b) > m:
                continue
            ans = max(ans, sum([x * (j-i+1) for x in b]))
    print(ans)

=======
Suggestion 8

def solve(N, M, A):
    if N == M:
        return sum([i * A[i] for i in range(1, N + 1)])
    elif N > M:
        return solve(M, M, A)
    else:
        A.sort()
        A = A[::-1]
        # print(A)
        B = [0] * (N + 1)
        for i in range(1, N + 1):
            B[i] = B[i - 1] + A[i - 1]
        # print(B)
        ans = 0
        for i in range(1, N + 1):
            ans = max(ans, B[i] + (M - i) * A[i - 1])
        return ans

=======
Suggestion 9

def max_subarray_sum(a, m):
    max_sum = 0
    for i in range(len(a) - m + 1):
        subarray_sum = 0
        for j in range(i, i + m):
            subarray_sum += a[j] * (j - i + 1)
        max_sum = max(max_sum, subarray_sum)
    return max_sum

=======
Suggestion 10

def main():

    N, M = map(int, input().split())
    A = list(map(int, input().split()))

    A = sorted(A, reverse=True)
    A = A[:M]
    A = sorted(A)

    result = 0
    for i in range(len(A)):
        result += (i + 1) * A[i]

    print(result)

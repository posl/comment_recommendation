Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    n,m,k = map(int,input().split())
    a = list(map(int,input().split()))
    b = list(map(int,input().split()))
    a_sum = sum(a)
    b_sum = sum(b)
    if a_sum + b_sum <= k:
        print(n+m)
        return
    time = k
    count = 0
    i = 0
    j = 0
    while time >= 0 and i < n and j < m:
        if a[i] <= b[j]:
            time -= a[i]
            count += 1
            i += 1
        else:
            time -= b[j]
            count += 1
            j += 1
    while time >= 0 and i < n:
        time -= a[i]
        count += 1
        i += 1
    while time >= 0 and j < m:
        time -= b[j]
        count += 1
        j += 1
    print(count-1)

=======
Suggestion 2

def main():
    N, M, K = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    sum = 0
    i = 0
    j = 0
    #print(A, B)
    while True:
        if i < N and j < M:
            if A[i] <= B[j]:
                if sum + A[i] > K:
                    break
                else:
                    sum += A[i]
                    i += 1
            else:
                if sum + B[j] > K:
                    break
                else:
                    sum += B[j]
                    j += 1
        elif i < N:
            if sum + A[i] > K:
                break
            else:
                sum += A[i]
                i += 1
        elif j < M:
            if sum + B[j] > K:
                break
            else:
                sum += B[j]
                j += 1
        else:
            break
    print(i+j)

=======
Suggestion 3

def main():
    n,m,k = [int(x) for x in input().split()]
    a = [int(x) for x in input().split()]
    b = [int(x) for x in input().split()]
    a_sum = [0 for i in range(n+1)]
    b_sum = [0 for i in range(m+1)]
    for i in range(n):
        a_sum[i+1] = a_sum[i] + a[i]
    for i in range(m):
        b_sum[i+1] = b_sum[i] + b[i]
    ans = 0
    j = m
    for i in range(n+1):
        if a_sum[i] > k:
            break
        while b_sum[j] > k - a_sum[i]:
            j -= 1
        ans = max(ans, i + j)
    print(ans)

=======
Suggestion 4

def main():
    n,m,k = map(int,input().split())
    a = list(map(int,input().split()))
    b = list(map(int,input().split()))
    a_sum = sum(a)
    b_sum = sum(b)
    a_count = 0
    b_count = 0
    for i in range(n):
        if a_sum - a[i] <= k:
            a_count += 1
            a_sum -= a[i]
        else:
            break
    for j in range(m):
        if b_sum - b[j] <= k:
            b_count += 1
            b_sum -= b[j]
        else:
            break
    if a_count == n and b_count == m:
        print(n + m)
    elif a_count == n:
        print(n + b_count)
    elif b_count == m:
        print(m + a_count)
    else:
        print(max(a_count,b_count))
    return 0

=======
Suggestion 5

def main():
    n,m,k = map(int,input().split())
    a = list(map(int,input().split()))
    b = list(map(int,input().split()))
    a_sum = [0]
    b_sum = [0]
    for i in range(n):
        a_sum.append(a_sum[i]+a[i])
    for i in range(m):
        b_sum.append(b_sum[i]+b[i])
    ans = 0
    j = m
    for i in range(n+1):
        if a_sum[i]>k:
            break
        while a_sum[i]+b_sum[j]>k:
            j -= 1
        ans = max(ans,i+j)
    print(ans)

=======
Suggestion 6

def main():
    n,m,k = map(int,input().split())
    a = list(map(int,input().split()))
    b = list(map(int,input().split()))
    for i in range(1,n):
        a[i] += a[i-1]
    for i in range(1,m):
        b[i] += b[i-1]
    ans = 0
    j = m
    for i in range(n+1):
        if a[i] > k:
            break
        while j > 0 and b[j-1] > k - a[i]:
            j -= 1
        ans = max(ans,i+j)
    print(ans)

=======
Suggestion 7

def read_ints():
    return list(map(int, input().split()))

=======
Suggestion 8

def main():
    n, m, k = [int(i) for i in input().split()]
    a = [int(i) for i in input().split()]
    b = [int(i) for i in input().split()]
    a = sorted(a)
    b = sorted(b)
    if len(a) > len(b):
        a, b = b, a
    i = 0
    j = 0
    while i < len(a) and k >= a[i]:
        k -= a[i]
        i += 1
    while j < len(b) and k >= b[j]:
        k -= b[j]
        j += 1
    print(i + j)

=======
Suggestion 9

def solve():
    n, m, k = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    a = sorted(a)
    b = sorted(b)

    ans = 0
    for i in range(n):
        if k < a[i]:
            break
        k -= a[i]
        ans += 1

    for i in range(m):
        if k < b[i]:
            break
        k -= b[i]
        ans += 1

    print(ans)

=======
Suggestion 10

def main():
    pass

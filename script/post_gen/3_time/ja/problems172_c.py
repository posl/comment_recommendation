Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    n, m, k = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    a_sum = [0] * (n+1)
    b_sum = [0] * (m+1)

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
        ans = max(ans, i+j)
    print(ans)

=======
Suggestion 2

def main():
    n,m,k = map(int,input().split())
    a = list(map(int,input().split()))
    b = list(map(int,input().split()))
    sum_a = [0]
    sum_b = [0]
    for i in range(n):
        sum_a.append(sum_a[i] + a[i])
    for i in range(m):
        sum_b.append(sum_b[i] + b[i])
    ans = 0
    j = m
    for i in range(n+1):
        if sum_a[i] > k:
            break
        while sum_b[j] > k - sum_a[i]:
            j -= 1
        ans = max(ans,i+j)
    print(ans)
main()

=======
Suggestion 3

def main():
    n, m, k = map(int, input().split())
    a_list = list(map(int, input().split()))
    b_list = list(map(int, input().split()))

    a_sum_list = [0]
    for a in a_list:
        a_sum_list.append(a_sum_list[-1] + a)

    b_sum_list = [0]
    for b in b_list:
        b_sum_list.append(b_sum_list[-1] + b)

    max_count = 0
    a_count = 0
    b_count = 0
    while a_count <= n:
        if a_sum_list[a_count] > k:
            break
        while b_sum_list[b_count] <= k - a_sum_list[a_count]:
            b_count += 1
        max_count = max(max_count, a_count + b_count - 1)
        a_count += 1

    print(max_count)

=======
Suggestion 4

def main():
    N, M, K = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    Asum = [0]*(N+1)
    Bsum = [0]*(M+1)
    for i in range(N):
        Asum[i+1] = Asum[i] + A[i]
    for i in range(M):
        Bsum[i+1] = Bsum[i] + B[i]
    ans = 0
    j = M
    for i in range(N+1):
        if Asum[i] > K:
            break
        while Bsum[j] > K - Asum[i]:
            j -= 1
        ans = max(ans, i+j)
    print(ans)

=======
Suggestion 5

def main():
    N,M,K = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))

    Asum = [0]
    Bsum = [0]
    for i in range(N):
        Asum.append(Asum[i] + A[i])
    for i in range(M):
        Bsum.append(Bsum[i] + B[i])

    ans = 0
    j = M
    for i in range(N + 1):
        if Asum[i] > K:
            break
        while Bsum[j] > K - Asum[i]:
            j -= 1
        ans = max(ans, i + j)
    print(ans)

=======
Suggestion 6

def main():
    # input
    N, M, K = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))

    # compute
    A = [0] + A
    B = [0] + B
    for i in range(1, N+1):
        A[i] += A[i-1]
    for i in range(1, M+1):
        B[i] += B[i-1]

    ans = 0
    j = M
    for i in range(N+1):
        if A[i] > K:
            break
        while B[j] > K - A[i]:
            j -= 1
        ans = max(ans, i+j)

    # output
    print(ans)

=======
Suggestion 7

def main():
    n,m,k = map(int,input().split())
    a = list(map(int,input().split()))
    b = list(map(int,input().split()))
    time = 0
    cnt = 0
    for i in range(n):
        if time + a[i] <= k:
            time += a[i]
            cnt += 1
        else:
            break
    for i in range(m):
        if time + b[i] <= k:
            time += b[i]
            cnt += 1
        else:
            break
    print(cnt)

=======
Suggestion 8

def main():
    n, m, k = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    #累積和
    a_acc = [0]
    b_acc = [0]
    for i in range(n):
        a_acc.append(a_acc[i] + a[i])
    for i in range(m):
        b_acc.append(b_acc[i] + b[i])

    ans = 0
    j = m
    for i in range(n + 1):
        if a_acc[i] > k:
            break
        while b_acc[j] > k - a_acc[i]:
            j -= 1
        ans = max(ans, i + j)
    print(ans)

=======
Suggestion 9

def solve():
    N, M, K = list(map(int, input().split()))
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))

    sum_time = 0
    sum_book = 0

    while sum_time <= K:
        if len(A) == 0 and len(B) == 0:
            break
        elif len(A) == 0:
            sum_time += B.pop(0)
            sum_book += 1
        elif len(B) == 0:
            sum_time += A.pop(0)
            sum_book += 1
        else:
            if A[0] <= B[0]:
                sum_time += A.pop(0)
                sum_book += 1
            else:
                sum_time += B.pop(0)
                sum_book += 1

    print(sum_book - 1)

=======
Suggestion 10

def main():
    n,m,k = map(int,input().split())
    a = list(map(int,input().split()))
    b = list(map(int,input().split()))
    a_sum = sum(a)
    b_sum = sum(b)
    a_list = []
    b_list = []
    for i in range(n):
        a_list.append([a_sum,sum(a[:i+1])])
        a_sum -= a[i]
    for i in range(m):
        b_list.append([b_sum,sum(b[:i+1])])
        b_sum -= b[i]
    ans = 0
    for i in range(n):
        if a_list[i][1] > k:
            break
        for j in range(m):
            if a_list[i][1]+b_list[j][1] > k:
                break
            if a_list[i][1]+b_list[j][1] <= k:
                ans = max(ans,i+j+2)
    print(ans)

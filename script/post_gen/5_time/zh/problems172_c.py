Synthesizing 10/10 solutions

=======
Suggestion 1

def read_ints():
    return list(map(int,input().split()))

=======
Suggestion 2

def main():
    n,m,k = map(int,input().split())
    a = list(map(int,input().split()))
    b = list(map(int,input().split()))
    a_sum = 0
    b_sum = 0
    for i in range(n):
        a_sum += a[i]
        if a_sum > k:
            a_sum -= a[i]
            break
    for i in range(m):
        b_sum += b[i]
        if b_sum > k:
            b_sum -= b[i]
            break
    ans = max(i,j)
    while i >= 0:
        b_sum += b[j]
        j += 1
        while b_sum > k and i >= 0:
            b_sum -= b[i]
            i -= 1
        ans = max(ans,i+j)
    print(ans)

=======
Suggestion 3

def solve():
    N, M, K = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    A = [0] + A
    B = [0] + B
    for i in range(1, N + 1):
        A[i] += A[i - 1]
    for i in range(1, M + 1):
        B[i] += B[i - 1]
    ans = 0
    j = M
    for i in range(N + 1):
        if A[i] > K:
            break
        while A[i] + B[j] > K:
            j -= 1
        ans = max(ans, i + j)
    print(ans)

=======
Suggestion 4

def main():
    # 读入数据
    n,m,k = map(int,input().split())
    a = list(map(int,input().split()))
    b = list(map(int,input().split()))
    # 计算前缀和
    for i in range(1,n):
        a[i] += a[i-1]
    for i in range(1,m):
        b[i] += b[i-1]
    # 答案
    ans = 0
    # 遍历所有可能的读书数量
    for i in range(n+1):
        # j是从B桌读书的数量
        j = 0
        # 从A桌读书的数量为i
        # 从B桌读书的数量为j
        # 从A桌读书的时间为a[i-1]分钟
        # 从B桌读书的时间为b[j-1]分钟
        # 从A桌读书的时间+a桌读书的时间<=k
        # 从B桌读书的时间+b桌读书的时间<=k
        # 从A桌读书的数量<=n
        # 从B桌读书的数量<=m
        # 从A桌读书的数量+从B桌读书的数量<=n+m
        # 从A桌读书的数量+从B桌读书的数量<=n+m
        # 从A桌读书的数量+从B桌读书的数量<=n+m
        if a[i-1] > k:
            break
        while j <= m and b[j-1] > k - a[i-1]:
            j += 1
        ans = max(ans,i+j-1)
    print(ans)

=======
Suggestion 5

def solve():
    N, M, K = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    ans = 0
    cnt = 0
    for i in range(N):
        if cnt + A[i] > K:
            break
        cnt += A[i]
        ans += 1
    for i in range(M):
        while cnt + B[i] <= K and ans < N + M:
            cnt += B[i]
            ans += 1
        if cnt + B[i] > K:
            cnt -= A[ans - 1]
            ans -= 1
            break
    print(ans)

solve()

=======
Suggestion 6

def main():
    n, m, k = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    sum_a = [0] * (n + 1)
    sum_b = [0] * (m + 1)

    for i in range(n):
        sum_a[i + 1] = sum_a[i] + a[i]

    for i in range(m):
        sum_b[i + 1] = sum_b[i] + b[i]

    ans = 0
    j = m
    for i in range(n + 1):
        if sum_a[i] > k:
            break
        while sum_b[j] > k - sum_a[i]:
            j -= 1
        ans = max(ans, i + j)
    print(ans)

=======
Suggestion 7

def main():
    n,m,k = map(int,input().split())
    a = list(map(int,input().split()))
    b = list(map(int,input().split()))
    a = [0] + a
    b = [0] + b
    for i in range(1,n+1):
        a[i] += a[i-1]
    for i in range(1,m+1):
        b[i] += b[i-1]
    ans = 0
    j = m
    for i in range(n+1):
        if a[i] > k:
            break
        while b[j] > k - a[i]:
            j -= 1
        ans = max(ans,i+j)
    print(ans)

=======
Suggestion 8

def get_max_books(n, m, k, a, b):
    if n + m > k:
        return 0
    else:
        a_sum = 0
        b_sum = 0
        count = 0
        while a_sum + b_sum < k:
            if a_sum + a[count] < b_sum + b[count]:
                a_sum += a[count]
                count += 1
                if count == n:
                    return count
            else:
                b_sum += b[count]
                count += 1
                if count == m:
                    return count
        return count

=======
Suggestion 9

def main():
    n,m,k = map(int,input().split())
    a = list(map(int,input().split()))
    b = list(map(int,input().split()))
    sum = 0
    count = 0
    while sum < k:
        if len(a) > 0 and len(b) > 0:
            if a[0] < b[0]:
                if sum + a[0] <= k:
                    sum += a[0]
                    count += 1
                    a.pop(0)
                else:
                    break
            else:
                if sum + b[0] <= k:
                    sum += b[0]
                    count += 1
                    b.pop(0)
                else:
                    break
        elif len(a) > 0:
            if sum + a[0] <= k:
                sum += a[0]
                count += 1
                a.pop(0)
            else:
                break
        else:
            if sum + b[0] <= k:
                sum += b[0]
                count += 1
                b.pop(0)
            else:
                break

    print(count)

=======
Suggestion 10

def main():
    # 读入
    n, m, k = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    # 累積和を計算
    a_acc = [0]
    b_acc = [0]
    for i in range(n):
        a_acc.append(a_acc[i] + a[i])
    for i in range(m):
        b_acc.append(b_acc[i] + b[i])

    # 答えを求める
    ans = 0
    j = m
    for i in range(n + 1):
        if a_acc[i] > k:
            break
        while a_acc[i] + b_acc[j] > k:
            j -= 1
        ans = max(ans, i + j)
    print(ans)

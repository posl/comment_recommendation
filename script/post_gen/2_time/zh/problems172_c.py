Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

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
Suggestion 2

def main():
    n,m,k = map(int,input().split())
    a = list(map(int,input().split()))
    b = list(map(int,input().split()))
    a_sum = sum(a)
    b_sum = sum(b)
    if a_sum+b_sum <= k:
        print(n+m)
    else:
        b_sum = 0
        count = 0
        for i in range(n):
            b_sum += a[i]
            if b_sum <= k:
                count += 1
            else:
                break
        a_sum = 0
        for i in range(m):
            a_sum += b[i]
            if a_sum <= k:
                count += 1
            else:
                break
        print(count)

=======
Suggestion 3

def solve():
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
    #print(a_sum,b_sum)
    for i in range(n+1):
        if a_sum[i] > k:
            break
        for j in range(m+1):
            if a_sum[i]+b_sum[j] > k:
                break
            if i+j > ans:
                ans = i+j
    print(ans)

=======
Suggestion 4

def main():
    n, m, k = map(int, input().split())
    a = [int(i) for i in input().split()]
    b = [int(i) for i in input().split()]
    a = sorted(a)
    b = sorted(b)
    ans = 0
    while a or b:
        if a and b:
            if a[0] < b[0]:
                if k < a[0]:
                    break
                k -= a[0]
                ans += 1
                a.pop(0)
            else:
                if k < b[0]:
                    break
                k -= b[0]
                ans += 1
                b.pop(0)
        elif a:
            if k < a[0]:
                break
            k -= a[0]
            ans += 1
            a.pop(0)
        else:
            if k < b[0]:
                break
            k -= b[0]
            ans += 1
            b.pop(0)
    print(ans)

=======
Suggestion 5

def main():
    n, m, k = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    #累计时间
    for i in range(n-1):
        a[i+1] += a[i]
    for i in range(m-1):
        b[i+1] += b[i]
    
    #枚举A桌读书本数
    ans = 0
    for i in range(n):
        if a[i] > k:
            break
        #二分查找B桌读书本数
        ok = m
        ng = -1
        while abs(ok - ng) > 1:
            mid = (ok + ng) // 2
            if b[mid] > k - a[i]:
                ok = mid
            else:
                ng = mid
        ans = max(ans, i + ok + 2)
    #枚举B桌读书本数
    for i in range(m):
        if b[i] > k:
            break
        #二分查找A桌读书本数
        ok = n
        ng = -1
        while abs(ok - ng) > 1:
            mid = (ok + ng) // 2
            if a[mid] > k - b[i]:
                ok = mid
            else:
                ng = mid
        ans = max(ans, i + ok + 2)
    
    print(ans)

=======
Suggestion 6

def solve(n,m,k,alist,blist):
    sum = 0
    i = 0
    j = 0
    while(i < n and sum + alist[i] <= k):
        sum += alist[i]
        i += 1
    ans = i
    while(j < m and i >= 0):
        sum += blist[j]
        j += 1
        while(sum > k and i > 0):
            i -= 1
            sum -= alist[i]
        if sum <= k:
            ans = max(ans,i+j)
    return ans

=======
Suggestion 7

def main():
    N, M, K = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))

    # 读取A的书需要的时间
    A_time = [0]
    for a in A:
        A_time.append(A_time[-1] + a)

    # 读取B的书需要的时间
    B_time = [0]
    for b in B:
        B_time.append(B_time[-1] + b)

    # 二分查找
    ans = 0
    for i in range(N + 1):
        if A_time[i] > K:
            break
        # 二分查找
        ok = M + 1
        ng = -1
        while abs(ok - ng) > 1:
            mid = (ok + ng) // 2
            if A_time[i] + B_time[mid] <= K:
                ng = mid
            else:
                ok = mid
        ans = max(ans, i + ng)

    print(ans)

=======
Suggestion 8

def main():
    pass

=======
Suggestion 9

def solve():
    N, M, K = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    A_sum = [0] * (N + 1)
    B_sum = [0] * (M + 1)
    for i in range(N):
        A_sum[i + 1] = A_sum[i] + A[i]
    for i in range(M):
        B_sum[i + 1] = B_sum[i] + B[i]
    ans = 0
    j = M
    for i in range(N + 1):
        if A_sum[i] > K:
            break
        while B_sum[j] > K - A_sum[i]:
            j -= 1
        ans = max(ans, i + j)
    print(ans)
solve()

Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    n,m,k = map(int,input().split())
    a = list(map(int,input().split()))
    b = list(map(int,input().split()))
    sum = 0
    time = 0
    a_index = 0
    b_index = 0
    while time <= k and a_index < n and b_index < m:
        if a[a_index] <= b[b_index]:
            time += a[a_index]
            if time <= k:
                sum += 1
                a_index += 1
            else:
                break
        else:
            time += b[b_index]
            if time <= k:
                sum += 1
                b_index += 1
            else:
                break
    if a_index == n and b_index < m:
        while time <= k and b_index < m:
            time += b[b_index]
            if time <= k:
                sum += 1
                b_index += 1
            else:
                break
    elif b_index == m and a_index < n:
        while time <= k and a_index < n:
            time += a[a_index]
            if time <= k:
                sum += 1
                a_index += 1
            else:
                break
    print(sum)

=======
Suggestion 2

def main():
    #读入数据
    n,m,k = map(int,input().split())
    a = list(map(int,input().split()))
    b = list(map(int,input().split()))

    #计算前缀和
    a_sum = [0]
    b_sum = [0]
    for i in range(n):
        a_sum.append(a_sum[-1] + a[i])
    for i in range(m):
        b_sum.append(b_sum[-1] + b[i])

    #二分查找
    result = 0
    j = m
    for i in range(n+1):
        if a_sum[i] > k:
            break
        while b_sum[j] > k - a_sum[i]:
            j -= 1
        result = max(result,i+j)
    print(result)

=======
Suggestion 3

def solve():
    N,M,K = map(int,input().split())
    A = list(map(int,input().split()))
    B = list(map(int,input().split()))
    for i in range(1,N):
        A[i] += A[i-1]
    for i in range(1,M):
        B[i] += B[i-1]
    ans = 0
    j = M
    for i in range(N+1):
        if A[i] > K:
            break
        while B[j-1] > K - A[i]:
            j -= 1
        ans = max(ans,i+j)
    print(ans)

=======
Suggestion 4

def main():
    N, M, K = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))

    a_sum = [0]
    b_sum = [0]
    for i in range(N):
        a_sum.append(a_sum[i] + A[i])
    for i in range(M):
        b_sum.append(b_sum[i] + B[i])

    ans = 0
    j = M
    for i in range(N+1):
        if a_sum[i] > K:
            break
        while b_sum[j] > K - a_sum[i]:
            j -= 1
        ans = max(ans, i+j)
    print(ans)

=======
Suggestion 5

def solve():
    N, M, K = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    A_sum = [0]
    B_sum = [0]
    for i in range(N):
        A_sum.append(A_sum[i] + A[i])
    for i in range(M):
        B_sum.append(B_sum[i] + B[i])
    ans = 0
    j = M
    for i in range(N + 1):
        if A_sum[i] > K:
            break
        while B_sum[j] > K - A_sum[i]:
            j -= 1
        ans = max(ans, i + j)
    print(ans)

=======
Suggestion 6

def main():
    n,m,k=map(int,input().split())
    a=list(map(int,input().split()))
    b=list(map(int,input().split()))
    ans=0
    time=0
    while time<=k:
        if len(a)==0 and len(b)==0:
            break
        elif len(a)==0:
            time+=b.pop(0)
            ans+=1
        elif len(b)==0:
            time+=a.pop(0)
            ans+=1
        elif a[0]<b[0]:
            time+=a.pop(0)
            ans+=1
        else:
            time+=b.pop(0)
            ans+=1
    print(ans-1)

=======
Suggestion 7

def main():
    pass

=======
Suggestion 8

def main():
    N, M, K = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
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
        while A[i] + B[j] > K:
            j -= 1
        ans = max(ans, i+j)
    print(ans)

=======
Suggestion 9

def main():
    n,m,k = map(int,input().split())
    a = list(map(int,input().split()))
    b = list(map(int,input().split()))
    a_sum = sum(a)
    b_sum = sum(b)
    a.append(0)
    b.append(0)
    a_index = n
    b_index = m
    a_time = 0
    b_time = 0
    while a_time+b_time<k:
        if a_time+b_time+a[a_index]>k:
            a_time = k - b_time
            break
        if a_time+b_time+b[b_index]>k:
            b_time = k - a_time
            break
        if a[a_index]>b[b_index]:
            b_time += b[b_index]
            b_index -= 1
        else:
            a_time += a[a_index]
            a_index -= 1
    print(a_index+b_index)
main()

=======
Suggestion 10

def solve():
    N,M,K = map(int,input().split())
    A = list(map(int,input().split()))
    B = list(map(int,input().split()))
    A.append(0)
    B.append(0)
    A.sort()
    B.sort()
    ans = 0
    i = 0
    j = 0
    while K > 0:
        if i < N and j < M:
            if A[i] < B[j]:
                if K > A[i]:
                    K -= A[i]
                    ans += 1
                    i += 1
                else:
                    break
            else:
                if K > B[j]:
                    K -= B[j]
                    ans += 1
                    j += 1
                else:
                    break
        elif i < N:
            if K > A[i]:
                K -= A[i]
                ans += 1
                i += 1
            else:
                break
        elif j < M:
            if K > B[j]:
                K -= B[j]
                ans += 1
                j += 1
            else:
                break
        else:
            break
    print(ans)

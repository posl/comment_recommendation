Synthesizing 9/10 solutions

=======
Suggestion 1

def main():
    N=int(input())
    A=list(map(int,input().split()))
    S=sum(A)
    ans=float('inf')
    s=0
    for i in range(N-1):
        s+=A[i]
        ans=min(ans,abs(S-2*s))
    print(ans)

=======
Suggestion 2

def main():
    N = int(input())
    A = [int(x) for x in input().split()]
    #print(N, A)

    #P,Q,R,S分别为B,C,D,E中的元素之和
    #当P,Q,R,S中的最大值和最小值的绝对差值较小时，Snuke会更快乐。
    #请找出P,Q,R,S中最大和最小的绝对差值的最小可能。

    #P,Q,R,S中的最大值和最小值的绝对差值
    #最大值：max(P,Q,R,S)
    #最小值：min(P,Q,R,S)
    #P,Q,R,S中的最大值和最小值的绝对差值 = max(P,Q,R,S) - min(P,Q,R,S)
    #P,Q,R,S中的最大值和最小值的绝对差值的最小可能
    # = min(max(P,Q,R,S) - min(P,Q,R,S))

    #1. 3次切割，4个（非空）连续的子序列
    #2. 切割的位置可以自由选择
    #3. 最大值和最小值的绝对差值较小时，Snuke会更快乐
    #4. 找出P,Q,R,S中最大和最小的绝对差值的最小可能
    #5. 1 <= N <= 2*10^5
    #6. 1 <= A_i <= 10^9
    #7. 输入的所有数值都是整数

    #1. 3次切割，4个（非空）连续的子序列
    #2. 切割的位置可以自由选择
    #3. 最大值和最小值的绝对差值较小时，Snuke会更快乐
    #4. 找出P,Q,R,S中最大和最小的绝对差值的最小可能
    #5. 1 <= N <= 2

=======
Suggestion 3

def main():
    N = int(input())
    A = list(map(int, input().split()))
    # 3切割，4个连续子序列
    # 4个连续子序列，最大值最小值差值最小
    # 1 2 3 4 5 6 7
    # 1 2 3 4 5 6 7 8
    # 1 2 3 4 5 6 7 8 9
    # 1 2 3 4 5 6 7 8 9 10
    # 1 2 3 4 5 6 7 8 9 10 11
    # 1 2 3 4 5 6 7 8 9 10 11 12
    # 1 2 3 4 5 6 7 8 9 10 11 12 13
    # 1 2 3 4 5 6 7 8 9 10 11 12 13 14
    # 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15
    # 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16
    # 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17
    # 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18


    # 1 2 3 4 5 6 7 8 9
    # 1 2 3 4 5 6 7 8
    # 1 2 3 4 5 6 7
    # 1 2 3 4 5 6
    # 1 2 3 4 5
    # 1 2 3 4
    # 1 2

=======
Suggestion 4

def get_min_max_diff(array):
    n = len(array)
    if n < 4:
        return 0
    if n == 4:
        return min(array[3] - array[0], array[2] - array[1])
    if n == 5:
        return min(array[4] - array[0], array[3] - array[1], array[2] - array[2])
    if n == 6:
        return min(array[5] - array[0], array[4] - array[1], array[3] - array[2])
    if n == 7:
        return min(array[6] - array[0], array[5] - array[1], array[4] - array[2], array[3] - array[3])

    array.sort()
    return min(array[n-1] - array[0], array[n-2] - array[1], array[n-3] - array[2], array[n-4] - array[3])

=======
Suggestion 5

def solve():
    N = int(input())
    A = [int(x) for x in input().split()]
    B = [0] * (N+1)
    C = [0] * (N+1)
    D = [0] * (N+1)
    E = [0] * (N+1)
    for i in range(N):
        B[i+1] = B[i] + A[i]
    for i in range(N):
        C[i+1] = C[i] + A[i]
    for i in range(N):
        D[i+1] = D[i] + A[i]
    for i in range(N):
        E[i+1] = E[i] + A[i]
    for i in range(N):
        C[i+1] = max(C[i], C[i+1])
    for i in range(N):
        D[i+1] = max(D[i], D[i+1])
    for i in range(N):
        E[i+1] = max(E[i], E[i+1])
    for i in range(N):
        C[i+1] = min(C[i], C[i+1])
    for i in range(N):
        D[i+1] = min(D[i], D[i+1])
    for i in range(N):
        E[i+1] = min(E[i], E[i+1])
    ans = 10**9
    for i in range(1, N-1):
        b = B[i]
        c = C[i]
        d = D[i]
        e = E[i]
        ans = min(ans, max(b, c, d, e) - min(b, c, d, e))
    print(ans)

=======
Suggestion 6

def find_min_diff(a):
    a.sort()
    n = len(a)
    min_diff = 1000000000
    for i in range(0, n-3):
        p = a[i]
        q = a[i+1]
        r = a[n-2]
        s = a[n-1]
        diff = max(p, q, r, s) - min(p, q, r, s)
        if diff < min_diff:
            min_diff = diff
    return min_diff

n = int(input())
a = [int(x) for x in input().split()]
print(find_min_diff(a))

=======
Suggestion 7

def main():
    n = int(input())
    a = list(map(int, input().split()))
    s = [0] * (n + 1)
    for i in range(n):
        s[i + 1] = s[i] + a[i]
    ans = float('inf')
    for i in range(1, n - 2):
        for j in range(i + 1, n - 1):
            x = s[i]
            y = s[j] - s[i]
            z = s[n] - s[j]
            ans = min(ans, max(x, y, z) - min(x, y, z))
            ans = min(ans, max(x, y, z) - min(x, y, z))
    print(ans)

=======
Suggestion 8

def split_list(list1):
    list2=[]
    for i in range(len(list1)):
        list2.append(sum(list1[:i+1]))
    return list2

N=int(input())
A=list(map(int,input().split()))
A1=split_list(A)
A1.sort()
A2=A1[::-1]
A3=A2[0]-A2[-1]
print(A3)

=======
Suggestion 9

def get_max_min_diff(a):
    # 1.先将a排序
    a.sort()
    # 2.找出最大值和最小值
    max = a[-1] + a[-2] + a[-3]
    min = a[0] + a[1] + a[2]
    return max - min

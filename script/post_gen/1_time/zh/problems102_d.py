Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N = int(input())
    A = list(map(int, input().split()))
    #A = [3, 2, 4, 1, 2]
    #A = [10, 71, 84, 33, 6, 47, 23, 25, 52, 64]
    #A = [1, 2, 3, 1000000000, 4, 5, 6]
    #A = [1, 2, 3, 4, 5, 6, 7]
    #A = [1, 2, 3, 4, 5, 6]
    #A = [1, 2, 3, 4, 5]
    #A = [1, 2, 3, 4]
    #A = [1, 2, 3]
    #A = [1, 2]
    #A = [1]
    #A = [3, 2, 4, 1, 2]
    #A = [3, 2, 4, 1]
    #A = [3, 2, 4]
    #A = [3, 2]
    #A = [3]
    #A = [2, 4, 1, 2]
    #A = [2, 4, 1]
    #A = [2, 4]
    #A = [2]
    #A = [4, 1, 2]
    #A = [4, 1]
    #A = [4]
    #A = [1, 2]
    #A = [1]
    #A = [2]
    #A = [1, 2, 3, 4, 5, 6, 7]
    #A = [1, 2, 3, 4, 5, 6]
    #A = [1, 2, 3, 4, 5]
    #A = [1, 2, 3, 4]
    #A = [1, 2, 3]
    #A = [1, 2]
    #A = [1]
    #A = [2, 3,

=======
Suggestion 2

def get_max_min_diff(a):
    n = len(a)
    max_diff = 0
    for i in range(1, n-2):
        for j in range(i+1, n-1):
            for k in range(j+1, n):
                max_diff = max(max_diff, abs(sum(a[:i]) - sum(a[i:j]) - sum(a[j:k]) + sum(a[k:])))
    return max_diff

=======
Suggestion 3

def print_list(l):
    for i in l:
        print(i)

=======
Suggestion 4

def main():
    # 读入数据
    N = int(input())
    A = [int(i) for i in input().split()]
    # 累积和
    S = [0] * (N + 1)
    for i in range(N):
        S[i + 1] = S[i] + A[i]
    # 累积最大值
    M = [0] * (N + 1)
    for i in range(N):
        M[i + 1] = max(M[i], S[i + 1])
    # 答案
    ans = float('inf')
    for i in range(1, N - 1):
        # M[i] - S[i] : B + C
        # M[N] - M[i] : D + E
        ans = min(ans, max(M[i] - S[i], M[N] - M[i]))
    # 输出
    print(ans)

=======
Suggestion 5

def problems102_d():
    pass

=======
Suggestion 6

def main():
    N = int(input())
    A = list(map(int,input().split()))
    sumA = sum(A)
    P = 0
    Q = 0
    R = 0
    S = 0
    ans = 1000000000
    for i in range(N):
        P += A[i]
        if P >= sumA/2:
            break
    for j in range(i):
        Q += A[j]
        if Q >= P/2:
            break
    for k in range(j):
        R += A[k]
        if R >= Q/2:
            break
    S = sumA - P
    ans = min(ans,max(P-Q,Q-R,S-R)-min(P-Q,Q-R,S-R))
    P = 0
    Q = 0
    R = 0
    S = 0
    for i in range(N-1,-1,-1):
        P += A[i]
        if P >= sumA/2:
            break
    for j in range(i,N-1):
        Q += A[j]
        if Q >= P/2:
            break
    for k in range(j,N-1):
        R += A[k]
        if R >= Q/2:
            break
    S = sumA - P
    ans = min(ans,max(P-Q,Q-R,S-R)-min(P-Q,Q-R,S-R))
    print(ans)

=======
Suggestion 7

def main():
    n=int(input())
    a=list(map(int,input().split()))
    p,q,r,s=0,0,0,0
    ans=10**9
    for i in range(n-3):
        p+=a[i]
        q=0
        for j in range(i+1,n-2):
            q+=a[j]
            r=0
            for k in range(j+1,n-1):
                r+=a[k]
                s=sum(a)-p-q-r
                ans=min(ans,max(p,q,r,s)-min(p,q,r,s))
    print(ans)

main()

=======
Suggestion 8

def main():
    n = int(input())
    a = list(map(int, input().split()))
    s = sum(a)
    ans = float('inf')
    cur = 0
    for i in range(n - 1):
        cur += a[i]
        ans = min(ans, abs(s - 2 * cur))
    print(ans)

=======
Suggestion 9

def solve():
    n = int(input())
    a = list(map(int, input().split()))
    # print(n, a)

    # 1. 确定第一刀的位置
    # 2. 确定第二刀的位置
    # 3. 确定第三刀的位置
    # 4. 计算最大最小值
    # 5. 比较最大最小值的差值

    # 1. 确定第一刀的位置
    # 2. 确定第二刀的位置
    # 3. 确定第三刀的位置
    # 4. 计算最大最小值
    # 5. 比较最大最小值的差值
    # 1. 确定第一刀的位置
    # 2. 确定第二刀的位置
    # 3. 确定第三刀的位置
    # 4. 计算最大最小值
    # 5. 比较最大最小值的差值
    # 1. 确定第一刀的位置
    # 2. 确定第二刀的位置
    # 3. 确定第三刀的位置
    # 4. 计算最大最小值
    # 5. 比较最大最小值的差值
    # 1. 确定第一刀的位置
    # 2. 确定第二刀的位置
    # 3. 确定第三刀的位置
    # 4. 计算最大最小值
    # 5. 比较最大最小值的差值
    # 1. 确定第一刀的位置
    # 2. 确定第二刀的位置
    # 3. 确定第三刀的位置
    # 4. 计算最大最小值
    #

=======
Suggestion 10

def main():
    n = int(input())
    a = list(map(int, input().split()))
    maxs = [a[0]]
    mins = [a[0]]
    for i in range(1, n):
        maxs.append(max(maxs[i-1], a[i]))
        mins.append(min(mins[i-1], a[i]))
    ans = 0
    for i in range(n-1):
        ans = max(ans, abs(maxs[i]-mins[i+1]))
    print(ans)

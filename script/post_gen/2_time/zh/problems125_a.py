Synthesizing 9/10 solutions

=======
Suggestion 1

def main():
    n, k = map(int, input().split())
    s = input()
    ans = 0
    for i in range(n):
        if s[i] == '0':
            ans += 1
        else:
            if k > 0:
                k -= 1
                ans += 1
            else:
                break
    print(ans)

=======
Suggestion 2

def solve():
    N, K = map(int, input().split())
    S = input()
    # print(N, K, S)

    # 1. 将字符串S转化为一个数组A，其中A[i]表示第i个人的姿势
    A = []
    for i in range(N):
        if S[i] == '0':
            A.append(0)
        else:
            A.append(1)
    # print(A)

    # 2. 计算从左到右连续站立的人的数量
    #    为了计算方便，我们将连续站立的人的数量的数组表示为B
    #    B[i]表示从左到右连续站立的人的数量
    B = []
    tmp = 0
    for i in range(N):
        if A[i] == 0:
            tmp += 1
        else:
            tmp = 0
        B.append(tmp)
    # print(B)

    # 3. 计算从右到左连续站立的人的数量
    #    为了计算方便，我们将连续站立的人的数量的数组表示为C
    #    C[i]表示从右到左连续站立的人的数量
    C = []
    tmp = 0
    for i in range(N-1, -1, -1):
        if A[i] == 0:
            tmp += 1
        else:
            tmp = 0
        C.append(tmp)
    C.reverse()
    # print(C)

    # 4. 计算最终结果
    #    D[i]表示最多经过i个方向后连续站立的人的最大可能数量
    #    D[i] = max(B[j] + C[j+i] for j in range(N-i))
    D = []
    for i in range(K+1):
        tmp = 0
        for j in range(N-i):
            tmp = max(tmp, B[j]+C[j+i])
        D.append(tmp)
    # print(D)
    print(max(D))

solve()

=======
Suggestion 3

def main():
    n, k = map(int, input().split())
    s = input()
    # print(n, k, s)
    # print(s.count('0'), s.count('1'))
    if s.count('0') <= k:
        print(n)
        return
    ans = 0
    for i in range(n):
        j = i
        while j < n and s[j] == '0':
            j += 1
        ans = max(ans, j - i)
        k -= 1
        if k < 0:
            break
    print(ans)

=======
Suggestion 4

def main():
    pass

=======
Suggestion 5

def main():
    # 读入数据
    n, k = map(int, input().split())
    s = input()

    # 求解
    # 以0开始的连续1的个数
    # 以1开始的连续0的个数
    # 以0开始的连续1的个数
    # 以1开始的连续0的个数
    # ...
    # 以1开始的连续0的个数
    # 以0开始的连续1的个数
    # 以1开始的连续0的个数
    # 以0开始的连续1的个数
    # 以1开始的连续0的个数
    # 以0开始的连续1的个数
    # 以1开始的连续0的个数
    # 以0开始的连续1的个数
    # 以1开始的连续0的个数
    # 以0开始的连续1的个数
    # 以1开始的连续0的个数
    # 以0开始的连续1的个数
    # 以1开始的连续0的个数
    # 以0开始的连续1的个数
    # 以1开始的连续0的个数
    # 以0开始的连续1的个数
    # ...
    # 以1开始的连续0的个数
    # 以0开始的连续1的个数
    # 以1开始的连续0的个数
    # 以0开始的连续1的个数
    # 以1开始的连续0的个数
    # 以0开始的连续1的个数
    # ...
    # 以1开始的连续0的个数
    # 以0开始的连续1的个数
    # 以1开始的连续0的个数
    # 以0开始的连续1的个数

    # 以0开始的连

=======
Suggestion 6

def main():
    n, k = map(int, input().split())
    s = input()
    ans = 0
    for i in range(n-1):
        if s[i] != s[i+1]:
            ans += 1
    print(min(ans+2*k, n-1))

=======
Suggestion 7

def solve():
    N, K = map(int, input().split())
    S = input()
    S = list(S)
    S = [int(s) for s in S]
    # print(S)
    # print(K)
    # print(N)
    cnt = 0
    for i in range(N - 1):
        if S[i] == S[i + 1]:
            cnt += 1
    # print(cnt)
    ans = cnt + 2 * K
    if ans > N - 1:
        ans = N - 1
    print(ans)

=======
Suggestion 8

def main():
    n,k=map(int,input().split())
    s=input()
    t=[0]*(n+1)
    for i in range(n):
        t[i+1]=t[i]+int(s[i])
    ans=0
    for i in range(n):
        l=max(0,i-k)
        r=min(n,i+k)
        ans=max(ans,t[r]-t[l])
    print(ans)

=======
Suggestion 9

def main():
    # 读入数据
    N, K = map(int, input().split())
    S = input()

    # 计算连续站立的人的最大可能数量
    max_count = 0
    count = 0
    for i in range(N):
        if S[i] == "0":
            count += 1
        else:
            if K > 0:
                K -= 1
                count += 1
            else:
                count -= 1
        if count > max_count:
            max_count = count

    # 输出结果
    print(max_count)

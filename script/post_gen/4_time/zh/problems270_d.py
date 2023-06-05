Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    N,K = map(int,input().split())
    A = list(map(int,input().split()))
    A.append(N+1)
    ans = 0
    for i in range(K):
        ans += max(0,A[i+1]-A[i]-1)
    print(N-ans)

=======
Suggestion 2

def main():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    A.append(N + 1)
    ans = 0
    s = 0
    for i in range(K):
        if A[i + 1] - A[i] > ans:
            ans = A[i + 1] - A[i] - 1
            s = A[i]
    print(s)
    print(ans)
    return

main()

=======
Suggestion 3

def problem270_d():
    pass

=======
Suggestion 4

def solve(n, k, a):
    ans = 0
    for i in range(k):
        ans += a[i]
    return ans - a[k - 1] // 2

n, k = map(int, input().split())
a = list(map(int, input().split()))
print(solve(n, k, a))

=======
Suggestion 5

def main():
    N,K=map(int,input().split())
    A=list(map(int,input().split()))
    ans=0
    for i in range(K-1,-1,-1):
        if N>=A[i]:
            ans+=N//A[i]
            N%=A[i]
    print(ans)

main()

=======
Suggestion 6

def cal_max(a, k):
    if k == 0:
        return a
    else:
        return cal_max(a - (a & -a), k - 1)

=======
Suggestion 7

def solve():
    # 读入数据
    N, K = map(int, input().split())
    A = list(map(int, input().split()))

    # 贪心法
    ans = 0
    # 从大到小排序
    A.sort(reverse=True)
    # 从大到小遍历
    for i in range(K):
        # 从大到小遍历
        for j in range(A[i]):
            # 如果N为0，跳出循环
            if N == 0:
                break
            # 否则N减1
            N -= 1
            # ans加1
            ans += 1
    # 输出结果
    print(ans)

solve()

=======
Suggestion 8

def main():
    N,K = map(int,input().split())
    A = list(map(int,input().split()))
    ans = 0
    for i in range(K-1,-1,-1):
        if N >= A[i]:
            ans += (N//A[i])*(i+1)
            N %= A[i]
    print(ans)

=======
Suggestion 9

def get_problem_description():
    return "270D"

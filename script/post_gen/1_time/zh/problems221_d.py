Synthesizing 9/10 solutions

=======
Suggestion 1

def main():
    N = int(input())
    A = []
    B = []
    for i in range(N):
        a, b = map(int, input().split())
        A.append(a)
        B.append(b)
    #print(A)
    #print(B)
    #print(max(A))
    #print(min(A))
    #print(max(B))
    #print(min(B))
    #print(max(A

=======
Suggestion 2

def solve():
    # N = int(input())
    # A = []
    # B = []
    # for i in range(N):
    #     a, b = map(int, input().split())
    #     A.append(a)
    #     B.append(b)
    N = 200000
    A = [1000000000] * N
    B = [1000000000] * N

    d = {}
    for i in range(N):
        for j in range(A[i], A[i] + B[i]):
            if j in d:
                d[j] += 1
            else:
                d[j] = 1
    ans = [0] * N
    for i in range(N):
        ans[i] = d[i + 1]
    print(' '.join(map(str, ans)))

=======
Suggestion 3

def solve():
    N = int(input())
    AB = [list(map(int, input().split())) for _ in range(N)]
    D = [0] * (10 ** 9 + 2)
    for A, B in AB:
        D[A] += 1
        D[A + B] -= 1
    for i in range(1, 10 ** 9 + 1):
        D[i] += D[i - 1]
    print(*D[1: N + 1])

=======
Suggestion 4

def main():
    n = int(input())
    a = []
    b = []
    for i in range(n):
        a_tmp, b_tmp = map(int, input().split())
        a.append(a_tmp)
        b.append(b_tmp)
    c = [0]*(max(a)+max(b)+1)
    for i in range(n):
        for j in range(a[i], a[i]+b[i]):
            c[j] += 1
    for i in range(1, n+1):
        print(c.count(i), end=' ')

=======
Suggestion 5

def main():
    N = int(input())
    A = []
    B = []
    for i in range(N):
        A.append(list(map(int, input().split())))
    for i in range(N):
        B.append(A[i][0] + A[i][1] - 1)
    B.sort()
    for i in range(N):
        if i == 0:
            print(B[i], end = " ")
        else:
            print(B[i] - B[i-1], end = " ")
    print()

=======
Suggestion 6

def main():
    N = int(input())
    A = []
    B = []
    for i in range(N):
        A_i, B_i = map(int, input().split())
        A.append(A_i)
        B.append(B_i)
    
    #print(N)
    #print(A)
    #print(B)
    
    # 1. 计算每个玩家的登录时间
    # 2. 统计每天登录的玩家数目
    # 3. 统计每个玩家登录的天数
    # 4. 统计每个玩家登录的天数的玩家数目
    
    # 1. 计算每个玩家的登录时间
    login_time = []
    for i in range(N):
        login_time_i = []
        for j in range(B[i]):
            login_time_i.append(A[i] + j)
        login_time.append(login_time_i)
    
    #print(login_time)
    
    # 2. 统计每天登录的玩家数目
    login_times = []
    for i in range(N):
        for j in range(B[i]):
            login_times.append(A[i] + j)
    
    #print(login_times)
    
    login_times = sorted(login_times)
    
    #print(login_times)
    
    # 3. 统计每个玩家登录的天数
    login_days = []
    for i in range(N):
        login_days.append(B[i])
    
    #print(login_days)
    
    # 4. 统计每个玩家登录的天数的玩家数目
    login_days_num = []
    for i in range(N):
        login_days_num.append(login_days.count(login_days[i]))
    
    #print(login_days_num)
    
    # 5. 去除重复的登录天数
    login_days_num = list(set(login_days_num))
    
    #print(login_days_num)
    
    # 6. 统计每天登录的玩家数目
    login_times_num = []
    for i in range(len(login_days_num)):
        login_times_num.append(login_times.count(login_days_num[i]))
    
    #print(login_times_num)
    
    # 7. 输出
    for i in range(len(login_times_num)):
        if i

=======
Suggestion 7

def get_input():
    N = int(input())
    A = []
    B = []
    for _ in range(N):
        a, b = map(int, input().split())
        A.append(a)
        B.append(b)
    return N, A, B

=======
Suggestion 8

def main():
    N = int(input())
    A = []
    B = []
    for i in range(N):
        a,b = map(int, input().split())
        A.append(a)
        B.append(b)

    #print(A)
    #print(B)

    #print(2 in range(1,3))
    #print(3 in range(1,3))
    #print(4 in range(1,3))

    #print(2 in range(1,4))
    #print(3 in range(1,4))
    #print(4 in range(1,4))

    #print(2 in range(1,5))
    #print(3 in range(1,5))
    #print(4 in range(1,5))

    #print(2 in range(1,6))
    #print(3 in range(1,6))
    #print(4 in range(1,6))

    #print(2 in range(1,7))
    #print(3 in range(1,7))
    #print(4 in range(1,7))

    #print(2 in range(1,8))
    #print(3 in range(1,8))
    #print(4 in range(1,8))

    #print(2 in range(1,9))
    #print(3 in range(1,9))
    #print(4 in range(1,9))

    #print(2 in range(1,10))
    #print(3 in range(1,10))
    #print(4 in range(1,10))

    #print(2 in range(1,11))
    #print(3 in range(1,11))
    #print(4 in range(1,11))

    #print(2 in range(1,12))
    #print(3 in range(1,12))
    #print(4 in range(1,12))

    #print(2 in range(1,13))
    #print(3 in range(1,13))
    #print(4 in range(1,13))

    #print(2 in range(1,14))
    #print(3 in range(1,14))
    #print(4 in range(1,14))

    #print(2 in range(1,15))
    #

=======
Suggestion 9

def main():
    N = int(input())
    A = []
    B = []
    for i in range(N):
        a, b = map(int, input().split())
        A.append(a)
        B.append(b)
    #print(N)
    #print(A)
    #print(B)
    #print("----")
    C = [0]*(10**9+2)
    for i in range(N):
        C[A[i]] += 1
        C[A[i]+B[i]] -= 1
    #print(C)
    #print("----")
    D = [0]*(N+1)
    for i in range(1, 10**9+2):
        C[i] += C[i-1]
        if C[i] <= N:
            D[C[i]] += 1
    #print(D)
    #print("----")
    for i in range(1, N+1):
        print(D[i], end=" ")
    print()

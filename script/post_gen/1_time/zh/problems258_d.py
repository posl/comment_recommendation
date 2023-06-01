Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N, X = map(int, input().split())
    AB = [list(map(int, input().split())) for _ in range(N)]
    AB.sort(key=lambda x: x[0] + x[1])
    ans = 0
    for i in range(N):
        ans += AB[i][0] + AB[i][1]
        if ans > X:
            print(i + 1)
            exit()
    print(N + 1)

=======
Suggestion 2

def main():
    pass

=======
Suggestion 3

def solve():
    N, X = map(int, input().split())
    AB = [list(map(int, input().split())) for _ in range(N)]
    A = [ab[0] for ab in AB]
    B = [ab[1] for ab in AB]
    # print(N, X)
    # print(A)
    # print(B)

    # 第i个阶段清除一次的时间
    # T1 = [A[i] + B[i] for i in range(N)]
    # print(T1)

    # 第i个阶段清除X次的时间
    T = [A[i] * X + B[i] for i in range(N)]
    # print(T)

    # 第i个阶段清除X次的时间的前缀和
    T_sum = [0] * N
    T_sum[0] = T[0]
    for i in range(1, N):
        T_sum[i] = T_sum[i - 1] + T[i]
    # print(T_sum)

    # 第i个阶段清除X次的时间的后缀和
    T_sum_r = [0] * N
    T_sum_r[N - 1] = T[N - 1]
    for i in range(N - 2, -1, -1):
        T_sum_r[i] = T_sum_r[i + 1] + T[i]
    # print(T_sum_r)

    ans = 0
    for i in range(N):
        if i == 0:
            ans = T_sum_r[i + 1] + (N - 1) * T[i]
        elif i == N - 1:
            ans = T_sum[i - 1] + (N - 1) * T[i]
        else:
            ans = min(ans, T_sum[i - 1] + T_sum_r[i + 1] + (N - 1) * T[i])
    print(ans)


solve()

=======
Suggestion 4

def main():
    n, x = map(int, input().split())
    ab = [list(map(int, input().split())) for _ in range(n)]
    a = [ab[i][0] for i in range(n)]
    b = [ab[i][1] for i in range(n)]
    # print(a)
    # print(b)
    # print(ab)
    # print(n)
    # print(x)

    # 二分探索
    left = 0
    right = 1000000000 * 1000000000
    while left < right:
        mid = (left + right) // 2
        # print("mid = ", mid)
        # print("left = ", left)
        # print("right = ", right)
        # print("check = ", check(mid, a, b, x))
        if check(mid, a, b, x):
            right = mid
        else:
            left = mid + 1

    print(left)

=======
Suggestion 5

def getMinTime(N,X,AB):
    if N == 1:
        return AB[0][0] + AB[0][1] * X
    else:
        minTime = AB[0][0] + AB[0][1] * X
        for i in range(1,N):
            time = AB[i][0] + AB[i][1] * X
            if time < minTime:
                minTime = time
        return minTime

=======
Suggestion 6

def main():
    n,x = map(int,input().split())
    data = []
    for i in range(n):
        data.append(list(map(int,input().split())))
    print(data)
    min_time = 10**9*n
    for i in range(1,n+1):
        sum_time = 0
        for j in range(n):
            if j == i-1:
                sum_time += data[j][0]+data[j][1]
            else:
                sum_time += data[j][1]
        if sum_time < min_time:
            min_time = sum_time
    print(min_time+x)

=======
Suggestion 7

def main():
    N, X = map(int, input().split())
    AB = [list(map(int, input().split())) for _ in range(N)]
    A = [AB[i][0] for i in range(N)]
    B = [AB[i][1] for i in range(N)]
    #print(N, X)
    #print(AB)
    #print(A)
    #print(B)
    #print(sum(A))
    #print(sum(B))
    #print(X)
    #print(X*sum(A))
    #print(X*sum(B))
    #print(sum(A)+sum(B))
    #print(sum(A)+sum(B)+X)
    #print(X*sum(A)+X*sum(B))
    #print(X*sum(A)+X*sum(B)+sum(A)+sum(B))
    print(X*sum(A)+X*sum(B)+sum(A)+sum(B))
    return

=======
Suggestion 8

def solve():
    N,X = map(int,input().split())
    AB = []
    for i in range(N):
        AB.append(list(map(int,input().split())))
    #print(AB)
    #print(N,X)
    min_time = 10**9*N
    for i in range(N):
        time = 0
        for j in range(N):
            if j <= i:
                time += AB[j][0] + AB[j][1]
            else:
                time += AB[j][1]
        #print(time)
        min_time = min(min_time,time)
    print(min_time+X)

=======
Suggestion 9

def main():
    N, X = map(int, input().split())
    AB = [list(map(int, input().split())) for _ in range(N)]
    # print(N, X)
    # print(AB)
    A = [0] * N
    B = [0] * N
    for i in range(N):
        A[i] = AB[i][0]
        B[i] = AB[i][1]
    # print(A)
    # print(B)
    min_time = 10 ** 20
    for i in range(N):
        time = A[i] * X + B[i] * (X - 1)
        if min_time > time:
            min_time = time
    print(min_time)

=======
Suggestion 10

def main():
    N, X = map(int, input().split())
    AB = [list(map(int, input().split())) for _ in range(N)]
    A = [ab[0] for ab in AB]
    B = [ab[1] for ab in AB]
    ans = 0
    for i in range(N):
        if B[i] > A[i]:
            ans += A[i] * X
        else:
            ans += B[i] * X
    print(ans)

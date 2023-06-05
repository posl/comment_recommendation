Synthesizing 9/10 solutions

=======
Suggestion 1

def solve():
    N, P, Q, R = map(int, input().split())
    A = list(map(int, input().split()))
    #print(N, P, Q, R)
    #print(A)
    dp = [[0 for _ in range(3)] for _ in range(N)]
    dp[0][0] = P * A[0]
    dp[0][1] = dp[0][0] + Q * A[0]
    dp[0][2] = dp[0][1] + R * A[0]
    for i in range(1, N):
        dp[i][0] = max(dp[i - 1][0], P * A[i])
        dp[i][1] = max(dp[i - 1][1], dp[i][0] + Q * A[i])
        dp[i][2] = max(dp[i - 1][2], dp[i][1] + R * A[i])
    print(dp[-1][2])

solve()

=======
Suggestion 2

def check(x,y,z,w):
    global a
    p=sum(a[x:y])
    q=sum(a[y:z])
    r=sum(a[z:w])
    if p==q and q==r:
        return True
    else:
        return False

n,p,q,r=map(int,input().split())
a=list(map(int,input().split()))
for i in range(n-3):
    for j in range(i+1,n-2):
        for k in range(j+1,n-1):
            for l in range(k+1,n):
                if check(i,j,k,l):
                    print('Yes')
                    exit()
print('No')

=======
Suggestion 3

def main():
    n,p,q,r = map(int,input().split())
    a = list(map(int,input().split()))
    a.sort()
    dp = [0]*n
    dp[0] = a[0]
    for i in range(1,n):
        dp[i] = dp[i-1] + a[i]
    #print(dp)
    ans = 0
    for i in range(n-1,2,-1):
        if dp[i] >= r:
            for j in range(i-1,1,-1):
                if dp[j] >= q+dp[i]:
                    for k in range(j-1,0,-1):
                        if dp[k] >= p+dp[j]:
                            ans = 1
                            break
                    if ans == 1:
                        break
                if ans == 1:
                    break
        if ans == 1:
            break
    if ans == 1:
        print("Yes")
    else:
        print("No")
main()

=======
Suggestion 4

def main():
    n, p, q, r = map(int, input().split())
    a = list(map(int, input().split()))

    # 从左到右计算A_{x}+A_{x+1}+...+A_{y-1}的最大值
    max_a = [0] * n
    max_a[0] = a[0]
    for i in range(1, n):
        max_a[i] = max(max_a[i - 1], a[i])

    # 从右到左计算A_{z}+A_{z+1}+...+A_{w-1}的最大值
    max_c = [0] * n
    max_c[n - 1] = a[n - 1]
    for i in range(n - 2, -1, -1):
        max_c[i] = max(max_c[i + 1], a[i])

    # 计算A_{y}+A_{y+1}+...+A_{z-1}的最大值
    s = [0] * n
    s[0] = a[0]
    for i in range(1, n):
        s[i] = s[i - 1] + a[i]

    # 计算结果
    ans = 'No'
    for i in range(1, n - 1):
        if p <= a[i] <= q and max_a[i - 1] >= p and max_c[i + 1] >= r and s[i - 1] >= p * (i - 1) and s[n - 1] - s[i] >= r * (n - i - 1):
            ans = 'Yes'
            break
    print(ans)

=======
Suggestion 5

def solve():
    N, P, Q, R = map(int, input().split())
    A = list(map(int, input().split()))
    maxA = [0] * N
    maxA[0] = A[0]
    for i in range(1, N):
        maxA[i] = max(maxA[i - 1], A[i])
    minA = [0] * N
    minA[N - 1] = A[N - 1]
    for i in range(N - 2, -1, -1):
        minA[i] = min(minA[i + 1], A[i])
    ans = 0
    for i in range(N):
        if (minA[i] <= P and P <= maxA[i] and minA[i] <= Q - P and Q - P <= maxA[i] and minA[i] <= R - Q + P and R - Q + P <= maxA[i]):
            ans += 1
    if ans > 0:
        print("Yes")
    else:
        print("No")

=======
Suggestion 6

def main():
    N, P, Q, R = map(int, input().split())
    A = list(map(int, input().split()))

    # 一开始，我认为这是一个组合问题，但是我不知道如何解决它。
    # 然后我发现，由于序列元素的限制，它可以被分解为三个子问题：
    # 1. A_x + A_{x+1}.+ ...+ A_{y-1} = P
    # 2. A_y + A_{y+1} = P+ ...+ A_{z-1} = Q
    # 3. A_z + A_{z+1} = Q+ ...+ A_{w-1} = R
    # 我们可以用动态规划来解决这个问题。
    # 我们将从左到右遍历序列，用以下变量来跟踪子问题的解决方案：
    # 1. P_left[i]：A_0 + A_1 + ... + A_i = P
    # 2. Q_left[i]：A_0 + A_1 + ... + A_i = Q
    # 3. R_left[i]：A_0 + A_1 + ... + A_i = R
    # 4. P_right[i]：A_i + A_{i+1} + ... + A_{N-1} = P
    # 5. Q_right[i]：A_i + A_{i+1} + ... + A_{N-1} = Q
    # 6. R_right[i]：A_i + A_{i+1} + ... + A_{N-1} = R
    # 我们可以通过以下方式更新这些变量：
    # 1. P_left[i] = max(P_left[i-1], A_i)
    # 2. Q_left[i] = max(Q_left[i-1], P_left[i] + A_i)
    # 3. R_left[i] = max(R_left[i-1], Q_left[i] + A_i)
    # 4. P_right[i] = max(P_right[i+1], A

=======
Suggestion 7

def solve():
    n, p, q, r = map(int, input().split())
    a = list(map(int, input().split()))

    max_a = [0] * n
    max_a[0] = a[0]
    for i in range(1, n):
        max_a[i] = max(max_a[i - 1], a[i])

    min_a = [0] * n
    min_a[0] = a[0]
    for i in range(1, n):
        min_a[i] = min(min_a[i - 1], a[i])

    ans = 0
    for i in range(n):
        if min_a[i] == a[i] and max_a[i] == a[i]:
            continue
        ans = max(ans, (p - 1) * a[i] + q * (max_a[i] - a[i]) + r * (a[i] - min_a[i]))
    print(ans)

solve()

=======
Suggestion 8

def main():
    N, P, Q, R = map(int, input().split())
    A = list(map(int, input().split()))
    #print(N, P, Q, R)
    #print(A)
    #print(len(A))
    if len(A) != N:
        print("No")
        return
    #print("ok")
    #print(A[0])
    #print(A[1])
    #print(A[2])
    #print(A[3])
    #print(A[4])
    #print(A[5])
    #print(A[6])
    #print(A[7])
    #print(A[8])
    #print(A[9])
    #print(A[10])
    #print(A[11])
    #print(A[12])
    #print(A[13])
    #print(A[14])
    #print(A[15])
    #print(A[16])
    #print(A[17])
    #print(A[18])
    #print(A[19])
    #print(A[20])
    #print(A[21])
    #print(A[22])
    #print(A[23])
    #print(A[24])
    #print(A[25])
    #print(A[26])
    #print(A[27])
    #print(A[28])
    #print(A[29])
    #print(A[30])
    #print(A[31])
    #print(A[32])
    #print(A[33])
    #print(A[34])
    #print(A[35])
    #print(A[36])
    #print(A[37])
    #print(A[38])
    #print(A[39])
    #print(A[40])
    #print(A[41])
    #print(A[42])
    #print(A[43])
    #print(A[44])
    #print(A[45])
    #print(A[46])
    #print(A[47])
    #print(A[48])
    #print(A[49])
    #print(A[50])
    #print(A[51])
    #print(A[52])
    #print(A[53])
    #print(A[54])
    #print(A[55])
    #print(A[56])
    #print(A[57])
    #print(A[58])
    #print(A[59])
    #print(A[60])

=======
Suggestion 9

def main():
    N, P, Q, R = map(int, input().split())
    A = list(map(int, input().split()))
    if N < 4:
        print("No")
        return
    #前缀和
    S = [0]*(N+1)
    for i in range(N):
        S[i+1] = S[i] + A[i]
    #print(S)
    #从左到右，找到满足条件的y
    y = 1
    while y < N-1:
        if S[y] >= P:
            break
        y += 1
    if y == N-1:
        print("No")
        return
    #从y开始，找到满足条件的z
    z = y + 1
    while z < N-1:
        if S[z] - S[y] >= Q:
            break
        z += 1
    if z == N-1:
        print("No")
        return
    #从z开始，找到满足条件的w
    w = z + 1
    while w < N:
        if S[w] - S[z] >= R:
            break
        w += 1
    if w == N:
        print("No")
        return
    print("Yes")

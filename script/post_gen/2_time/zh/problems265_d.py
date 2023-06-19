Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N, P, Q, R = map(int, input().split())
    A = list(map(int, input().split()))
    A.sort()
    # print(N, P, Q, R)
    # print(A)
    # print()
    # print()
    # pr

=======
Suggestion 2

def solve():
    n, p, q, r = map(int, input().split())
    a = list(map(int, input().split()))
    max_a = [0] * n
    min_a = [0] * n
    max_a[0] = a[0]
    min_a[0] = a[0]
    for i in range(1, n):
        max_a[i] = max(max_a[i - 1], a[i])
        min_a[i] = min(min_a[i - 1], a[i])
    ans = 0
    for i in range(n):
        if min_a[i] < p and max_a[i] > r:
            ans += 1
    print(ans)

=======
Suggestion 3

def solve():
    N, P, Q, R = map(int, input().split())
    A = list(map(int, input().split()))
    #print(N, P, Q, R)
    #print(A)
    ans = "No"
    for i in range(N-3+1):
        x = A[i]
        for j in range(i+1, N-2+1):
            y = A[j]
            for k in range(j+1, N-1+1):
                z = A[k]
                for l in range(k+1, N+1):
                    w = A[l]
                    if (x+y+z+w) == (P+Q+R) and (x+y) == P and (y+z) == Q and (z+w) == R:
                        ans = "Yes"
                        break
                if ans == "Yes":
                    break
            if ans == "Yes":
                break
        if ans == "Yes":
            break
    print(ans)

solve()

=======
Suggestion 4

def solve():
    # 读取数据
    N, p, q, r = map(int, input().split())
    A = list(map(int, input().split()))
    # 逆序累积和
    R = [0] * (N + 1)
    for i in range(N - 1, -1, -1):
        R[i] = max(R[i + 1], A[i])
    # 正序累积和
    S = [0] * (N + 1)
    for i in range(N):
        S[i + 1] = S[i] + A[i]
    # 二分查找
    ans = 'No'
    for i in range(1, N - 1):
        if p * i > q:
            break
        while True:
            j = N - 1
            while j > i and (S[j] - S[i]) * p > r:
                j -= 1
            if j <= i:
                break
            if (S[j] - S[i]) * p == r:
                if (S[j] - S[i]) * q == (S[i] - S[0]) * r:
                    ans = 'Yes'
                break
            if (S[j] - S[i]) * q > (S[i] - S[0]) * r:
                break
            if (S[j] - S[i]) * q == (S[i] - S[0]) * r:
                ans = 'Yes'
            if R[j] * q > (S[i] - S[0]) * r:
                break
            if R[j] * q == (S[i] - S[0]) * r:
                ans = 'Yes'
            break
    print(ans)

=======
Suggestion 5

def main():
    n, p, q, r = map(int, input().split())
    a = list(map(int, input().split()))

    # 从左到右扫描，记下当前最大值
    max_a = [0] * n
    max_a[0] = a[0]
    for i in range(1, n):
        max_a[i] = max(a[i], max_a[i - 1])

    # 从右到左扫描，记下当前最大值
    max_a_r = [0] * n
    max_a_r[n - 1] = a[n - 1]
    for i in range(n - 2, -1, -1):
        max_a_r[i] = max(a[i], max_a_r[i + 1])

    # 计算Q
    q_list = [0] * n
    for i in range(n):
        q_list[i] = q * a[i]

    # 计算Q
    q_list_r = [0] * n
    for i in range(n):
        q_list_r[i] = q * a[i]

    # 计算P
    p_list = [0] * n
    for i in range(n):
        p_list[i] = p * a[i]

    # 计算R
    r_list = [0] * n
    for i in range(n):
        r_list[i] = r * a[i]

    # 从左到右扫描，记下当前最大值
    max_q = [0] * n
    max_q[0] = q_list[0]
    for i in range(1, n):
        max_q[i] = max(q_list[i], max_q[i - 1])

    # 从右到左扫描，记下当前最大值
    max_q_r = [0] * n
    max_q_r[n - 1] = q_list[n - 1]
    for i in range(n - 2, -1, -1):
        max_q_r[i] = max(q_list[i], max_q_r[i + 1])

    # 从左到右扫描，记下当前最大值
    max_p = [0] * n

=======
Suggestion 6

def solve():
    N, P, Q, R = map(int, input().split())
    A = list(map(int, input().split()))
    max_p = A[0]
    min_p = A[0]
    max_q = A[0]
    min_q = A[0]
    max_r = A[0]
    min_r = A[0]
    for i in range(1, N):
        max_p = max(max_p, A[i])
        min_p = min(min_p, A[i])
        max_q = max(max_q, A[i] + max_p - P)
        min_q = min(min_q, A[i] + min_p - P)
        max_r = max(max_r, A[i] + max_q - Q)
        min_r = min(min_r, A[i] + min_q - Q)
    if max_r == R and min_r == R:
        print("Yes")
    else:
        print("No")

solve()

=======
Suggestion 7

def solve():
    N,P,Q,R = map(int, input().split())
    A = list(map(int, input().split()))
    # print(N, P, Q, R)
    # print(A)
    if N < 4:
        print("No")
        return

    # 从左到右扫描，找到满足条件的最小的x
    # 从左到右扫描，找到满足条件的最大的y
    # 从左到右扫描，找到满足条件的最大的z
    # 从左到右扫描，找到满足条件的最大的w
    # 判断是否存在满足条件的(x,y,z,w)
    # print("A[0] = ", A[0])
    # print("A[1] = ", A[1])
    # print("A[2] = ", A[2])
    # print("A[3] = ", A[3])
    # print("A[4] = ", A[4])
    # print("A[5] = ", A[5])
    # print("A[6] = ", A[6])
    # print("A[7] = ", A[7])
    # print("A[8] = ", A[8])
    # print("A[9] = ", A[9])
    # print("A[10] = ", A[10])
    # print("A[11] = ", A[11])
    # print("A[12] = ", A[12])
    # print("A[13] = ", A[13])
    # print("A[14] = ", A[14])
    # print("A[15] = ", A[15])
    # print("A[16] = ", A[16])
    # print("A[17] = ", A[17])
    # print("A[18] = ", A[18])
    # print("A[19] = ", A[19])
    # print("A[20] = ", A[20])
    # print("A[21] = ", A[21])
    # print("A[22] = ", A[22])
    # print("

=======
Suggestion 8

def main():
    N, P, Q, R = map(int, input().split())
    A = list(map(int, input().split()))

    # 从左到右扫描，找到最小的A_x
    x = 0
    for i in range(1, N):
        if A[i] < A[x]:
            x = i

    # 从右到左扫描，找到最大的A_w
    w = N - 1
    for j in range(N - 2, -1, -1):
        if A[j] > A[w]:
            w = j

    # 从左到右扫描，找到最小的A_y
    y = x
    for i in range(x + 1, w + 1):
        if A[i] < A[y]:
            y = i

    # 从右到左扫描，找到最大的A_z
    z = w
    for j in range(w - 1, y - 1, -1):
        if A[j] > A[z]:
            z = j

    # 从左到右扫描，找到最小的A_y
    y = x
    for i in range(x + 1, z + 1):
        if A[i] < A[y]:
            y = i

    # 从右到左扫描，找到最大的A_z
    z = w
    for j in range(w - 1, y - 1, -1):
        if A[j] > A[z]:
            z = j

    # 从左到右扫描，找到最小的A_y
    y = x
    for i in range(x + 1, z + 1):
        if A[i] < A[y]:
            y = i

    # 从右到左扫描，找到最大的A_z
    z = w
    for j in range(w - 1, y - 1, -1):
        if A[j] > A[z]:
            z = j

    # 从左到右扫描，找到最小的A_y
    y = x
    for i in range

=======
Suggestion 9

def main():
    n,p,q,r = map(int,input().split())
    a = list(map(int,input().split()))
    x = []
    y = []
    z = []
    w = []
    for i in range(n):
        if i == 0:
            x.append(a[i])
        else:
            x.append(x[i-1]+a[i])
    for i in range(n):
        if i == 0:
            y.append(a[i])
        elif i == 1:
            y.append(y[i-1]+a[i])
        else:
            y.append(y[i-1]+a[i])
    for i in range(n):
        if i == 0:
            z.append(a[i])
        elif i == 1:
            z.append(z[i-1]+a[i])
        elif i == 2:
            z.append(z[i-1]+a[i])
        else:
            z.append(z[i-1]+a[i])
    for i in range(n):
        if i == 0:
            w.append(a[i])
        elif i == 1:
            w.append(w[i-1]+a[i])
        elif i == 2:
            w.append(w[i-1]+a[i])
        elif i == 3:
            w.append(w[i-1]+a[i])
        else:
            w.append(w[i-1]+a[i])
    for i in range(n):
        if x[i] == p and y[i] == q and z[i] == r:
            print('Yes')
            break
        elif i == n-1:
            print('No')

=======
Suggestion 10

def solve():
    N, P, Q, R = map(int, input().split())
    A = list(map(int, input().split()))

    #累加和
    Asum = [0] * (N + 1)
    for i in range(N):
        Asum[i + 1] = Asum[i] + A[i]

    #最大值和最小值
    maxA = A[0]
    minA = A[0]
    for i in range(N):
        maxA = max(maxA, A[i])
        minA = min(minA, A[i])

    #最大值和最小值的累加和
    maxAsum = [0] * (N + 1)
    minAsum = [0] * (N + 1)
    for i in range(N):
        maxAsum[i + 1] = maxAsum[i] + maxA - A[i]
        minAsum[i + 1] = minAsum[i] + minA - A[i]

    #最大值和最小值的累加和的最大值和最小值
    maxmaxAsum = maxAsum[0]
    minminAsum = minAsum[0]
    for i in range(N):
        maxmaxAsum = max(maxmaxAsum, maxAsum[i])
        minminAsum = min(minminAsum, minAsum[i])

    #判断
    if maxmaxAsum - minminAsum <= R - P and maxAsum[N] - minAsum[N] == R - P and \
            maxAsum[N] - minAsum[N] == Q - R and Asum[N] == Q:
        print("Yes")
    else:
        print("No")

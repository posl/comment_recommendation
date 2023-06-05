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

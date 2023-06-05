def main():
    N, K, Q = input().split()
    N = int(N)
    K = int(K)
    Q = int(Q)
    A = []
    for i in range(Q):
        A.append(int(input()))
    # print(N, K, Q)
    # print(A)
    # print("end")
    # print("N = ", N)
    # print("K = ", K)
    # print("Q = ", Q)
    # print("A = ", A)
    #初始化分数
    score = []
    for i in range(N):
        score.append(K)
    # print("score = ", score)
    #开始游戏
    for i in range(Q):
        # print("A[", i, "] = ", A[i])
        for j in range(N):
            if j != (A[i] - 1):
                # print("j = ", j)
                score[j] = score[j] - 1
        # print("score = ", score)
    #判断是否幸存
    for i in range(N):
        if score[i] <= 0:
            print("No")
        else:
            print("Yes")

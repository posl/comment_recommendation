def main():
    # 读取输入
    N, K, Q = map(int, input().split())
    # print("N, K, Q:", N, K, Q)
    A = []
    for i in range(Q):
        A.append(int(input()))
    # print("A:", A)
    # 计算
    # 初始化
    score = [K] * N
    # print("score:", score)
    # 开始答题
    for i in range(Q):
        score[A[i] - 1] -= 1
    # print("score:", score)
    # 判断是否幸存
    for i in range(N):
        if score[i] > 0:
            print("Yes")
        else:
            print("No")

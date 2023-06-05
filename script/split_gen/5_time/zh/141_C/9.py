def main():
    # 读取N,K,Q
    N,K,Q = map(int, input().split())
    # 读取A_i
    A_i = [int(input()) for i in range(Q)]
    # 初始化玩家分数
    score = [K for i in range(N)]
    # 玩家分数变化
    for i in range(Q):
        score[A_i[i]-1] -= 1
    # 判断玩家是否幸存
    for i in range(N):
        if score[i] <= 0:
            print('No')
        else:
            print('Yes')

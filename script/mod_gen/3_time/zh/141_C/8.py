def main():
    #读入数据
    N, K, Q = map(int, input().split())
    A = [int(input()) for i in range(Q)]
    #初始化玩家得分
    score = [K-Q for i in range(N)]
    #计算玩家得分
    for i in range(Q):
        score[A[i]-1] += 1
    #输出
    for i in range(N):
        if score[i] > 0:
            print("Yes")
        else:
            print("No")

if __name__ == '__main__':
    main()
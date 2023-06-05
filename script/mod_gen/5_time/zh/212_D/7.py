def main():
    # 读入数据
    Q = int(input())
    # 初始化一个空的列表
    bag = []
    # 循环Q次
    for i in range(Q):
        # 读入操作类型
        P = int(input())
        # 如果是类型1或2
        if P == 1 or P == 2:
            # 读入整数X
            X = int(input())
            # 如果是类型1
            if P == 1:
                # 把整数X放进袋子里
                bag.append(X)
            # 如果是类型2
            else:
                # 对于袋子里的每个球
                for j in range(len(bag)):
                    # 用该整数加X替换写在上面的整数
                    bag[j] += X
        # 如果是类型3
        else:
            # 找到袋子里整数最小的球
            min_ball = min(bag)
            # 记录写在这个球上的整数
            ans = min_ball
            # 把它扔掉
            bag.remove(min_ball)
            # 打印记录的整数
            print(ans)

if __name__ == '__main__':
    main()
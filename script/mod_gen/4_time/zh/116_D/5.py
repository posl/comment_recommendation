def main():
    # 读入
    N, K = map(int, input().split())
    # 建立一个字典
    d = {}
    for i in range(N):
        t, d_ = map(int, input().split())
        if t not in d:
            d[t] = [d_]
        else:
            d[t].append(d_)
    # 按照美味程度排序
    for k in d.keys():
        d[k].sort(reverse=True)
    # 按照美味程度排序
    sushi = []
    for k in d.keys():
        sushi += d[k]
    sushi.sort(reverse=True)
    # print(sushi)
    # 从头开始吃K个
    # 1. 基本总美味
    base = sum(sushi[:K])
    # 2. 种类奖励
    kind = 0
    # 计算种类奖励
    for k in d.keys():
        if len(d[k]) > 1:
            kind += (len(d[k]) - 1) ** 2
    # 输出
    print(base + kind)

if __name__ == '__main__':
    main()
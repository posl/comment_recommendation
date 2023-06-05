def main():
    # 读入数据
    N, M = map(int, input().split())
    cakes = []
    for i in range(N):
        cakes.append(list(map(int, input().split())))
    # 找出最大值
    ans = 0
    for i in range(2 ** 3):
        # 从二进制数的最低位开始，判断该位是否为1
        # 如果是1，就把对应的蛋糕的值加起来
        # 如果是0，就把对应的蛋糕的值减去
        # 由于二进制数的最低位是1，所以先把蛋糕的值加起来
        total = 0
        for j in range(N):
            value = 0
            for k in range(3):
                if ((i >> k) & 1) == 1:
                    value += cakes[j][k]
                else:
                    value -= cakes[j][k]
            total += abs(value)
        # 更新答案
        ans = max(ans, total)
    # 打印答案
    print(ans)

def main():
    # 读入数据
    a, b, c = map(int, input().split())
    # 期望值
    ans = 0
    # 一共需要100次操作
    for i in range(100):
        # 三种硬币的数量
        x, y, z = a, b, c
        # 一共需要100次操作
        for j in range(100):
            # 三种硬币的数量
            x, y, z = x, y, z
            # 从三种硬币中随机取出一枚
            r = random.randint(0, x + y + z - 1)
            # 如果取出的是金币
            if r < x:
                # 金币数量减少1
                x -= 1
                # 金币和银币数量增加1
                y += 1
                z += 1
            # 如果取出的是银币
            elif r < x + y:
                # 银币数量减少1
                y -= 1
                # 金币和银币数量增加1
                x += 1
                z += 1
            # 如果取出的是铜币
            else:
                # 铜币数量减少1
                z -= 1
                # 三种硬币数量都增加1
                x += 1
                y += 1
            # 如果有100个相同颜色的硬币
            if x == 100 or y == 100 or z == 100:
                # 期望值增加j+1
                ans += j + 1
                # 退出循环
                break
    # 期望值除以100
    print(ans / 100)

if __name__ == '__main__':
    main()
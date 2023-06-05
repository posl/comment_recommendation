def main():
    # 输入
    n, m = map(int, input().split())
    # 初始化
    food = [0] * m
    # 循环输入
    for i in range(n):
        # 输入
        _, *a = map(int, input().split())
        # 循环统计
        for j in a:
            food[j - 1] += 1
    # 输出
    print(food.count(n))

if __name__ == '__main__':
    main()
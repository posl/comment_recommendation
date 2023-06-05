def main():
    # 读入数据
    n = int(input())
    # 用于存储结果
    queue = []
    # 用于存储A
    list_a = [-1 for i in range(2 ** 20)]
    # 用于存储h
    list_h = [-1 for i in range(2 ** 20)]
    # 用于存储x
    list_x = [-1 for i in range(2 ** 20)]
    # 用于存储t
    list_t = [-1 for i in range(2 ** 20)]
    for i in range(n):
        # 读入t和x
        t, x = map(int, input().split())
        list_t[i] = t
        list_x[i] = x
        # 如果t为1
        if t == 1:
            # 定义一个整数h为h=x_i。
            h = x
            # 当A_{h mod N}≠-1时，不断向h加1。我们可以证明，在这个问题的约束条件下，这个过程在有限迭代后结束。
            while list_a[h % (2 ** 20)] != -1:
                h += 1
            # 用x_i替换A_{h mod N}的值。
            list_a[h % (2 ** 20)] = x
            list_h[h % (2 ** 20)] = x
        # 如果t为2
        else:
            # 打印当时的A_{x_i mod N}的值。
            queue.append(list_a[x % (2 ** 20)])
    # 打印结果
    for i in queue:
        print(i)

if __name__ == '__main__':
    main()
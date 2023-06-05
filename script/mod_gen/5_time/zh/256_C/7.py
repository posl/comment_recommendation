def main():
    # 输入
    h1, h2, h3, w1, w2, w3 = map(int, input().split())
    # 用于计算的数组
    h = [h1, h2, h3]
    w = [w1, w2, w3]
    # 满足条件的数字写法的数量
    count = 0
    # 满足条件的数字写法的数量
    for i in range(1, h[0] + 1):
        for j in range(1, w[0] + 1):
            for k in range(1, h[1] + 1):
                for l in range(1, w[1] + 1):
                    for m in range(1, h[2] + 1):
                        for n in range(1, w[2] + 1):
                            if i + j == h[0] and i + k + m == h[1] and j + l + n == h[2] and k + l == w[0] and m + n == w[1] and i + l + m == w[2]:
                                count += 1
    # 输出
    print(count)

if __name__ == '__main__':
    main()
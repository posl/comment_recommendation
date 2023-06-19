def main():
    # 输入
    N, M = map(int, input().split())
    s_c = [list(map(int, input().split())) for _ in range(M)]
    # 处理
    # 1. 生成一个列表，用于存储最终结果
    result = [0 for _ in range(N)]
    # 2. 遍历输入的数据
    for s, c in s_c:
        # 2.1 如果输入的位置是第一位，且输入的数字是0，那么直接返回-1
        if s == 1 and c == 0:
            print(-1)
            return
        # 2.2 如果输入的位置不是第一位，且输入的数字是0，那么直接将该位置的数字设置为0
        if s != 1 and c == 0:
            result[s-1] = 0
        # 2.3 如果输入的位置是第一位，且输入的数字不是0，那么直接将该位置的数字设置为输入的数字
        if s == 1 and c != 0:
            result[s-1] = c
        # 2.4 如果输入的位置不是第一位，且输入的数字不是0，那么直接将该位置的数字设置为输入的数字
        if s != 1 and c != 0:
            result[s-1] = c
    # 3. 如果第一位是0，那么直接返回-1
    if result[0] == 0:
        print(-1)
        return
    # 4. 将列表转换成字符串，然后转换成整数
    result = int("".join(map(str, result)))
    # 5. 打印结果
    print(result)

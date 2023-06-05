def main():
    # 读取输入
    Q = int(input())
    query = [list(map(int, input().split())) for _ in range(Q)]
    # 用来记录结果
    result = []
    # 用来记录最小值
    min_value = 0
    # 用来记录最小值的个数
    min_value_count = 0
    # 用来记录最小值的和
    min_value_sum = 0
    # 用来记录最小值的平均值
    min_value_average = 0
    for i in range(Q):
        if query[i][0] == 1:
            # 如果是类型1，把整数放进袋子里
            min_value = min(query[i][1], min_value)
            min_value_count += 1
            min_value_sum += query[i][1]
            min_value_average = min_value_sum / min_value_count
        elif query[i][0] == 2:
            # 如果是类型2，对于袋子里的每个球，用该整数加X_i替换写在上面的整数
            min_value = min(query[i][1] + min_value, min_value)
            min_value_sum += query[i][1] * min_value_count
            min_value_average = min_value_sum / min_value_count
        else:
            # 如果是类型3，拿起袋子里整数最小的球（如果有多个这样的球，拿起其中一个）。记录写在这个球上的整数并把它扔掉。
            result.append(min_value)
            min_value_count -= 1
            min_value_sum -= min_value
            if min_value_count > 0:
                min_value_average = min_value_sum / min_value_count
            else:
                min_value_average = 0
    # 输出结果
    for i in range(len(result)):
        print(result[i])

if __name__ == '__main__':
    main()
def get_max_score(N, M, Q, array):
    # 从小到大排序
    array = sorted(array)
    # 记录每个位置的值
    value = [0 for i in range(N)]
    for i in range(N):
        value[i] = i + 1
    # 记录每个位置的值的总和
    sum = [0 for i in range(N)]
    for i in range(N):
        sum[i] = i + 1
    # 记录每个位置的值的总和的最大值
    max_sum = 0
    # 记录每个位置的值的总和的最大值的位置
    max_sum_index = 0
    # 记录每个位置的值的总和的最小值
    min_sum = 0
    # 记录每个位置的值的总和的最小值的位置
    min_sum_index = 0
    # 记录每个位置的值的总和的最大值的位置
    max_sum = 0
    # 记录每个位置的值的总和的最大值的位置
    max_sum_index = 0
    for i in range(Q):
        a = array[i][0]
        b = array[i][1]
        c = array[i][2]
        d = array[i][3]
        for j in range(a - 1, b):
            value[j] += c
            sum[j] += d
        if (max_sum < sum[b - 1]):
            max_sum = sum[b - 1]
            max_sum_index = b - 1
        if (min_sum > sum[a - 1]):
            min_sum = sum[a - 1]
            min_sum_index = a - 1
    sum[max_sum_index] = 0
    sum[min_sum_index] = 0
    for i in range(N):
        if (max_sum < sum[i]):
            max_sum = sum[i]
    return max_sum

if __name__ == '__main__':
    get_max_score()
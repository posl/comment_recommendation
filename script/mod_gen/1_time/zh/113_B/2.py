def judge_temperature(n,t,a,h):
    """
    n:地点个数
    t:海拔高度
    a:温度
    h:地点海拔高度列表
    """
    #计算平均温度
    temperature = t - a * 0.006
    #计算每个地点的平均温度
    temperature_list = []
    for i in range(n):
        temperature_list.append(temperature - h[i] * 0.006)
    #找到最接近的温度
    min_temperature = temperature_list[0]
    min_index = 0
    for i in range(n):
        if abs(temperature_list[i] - temperature) < abs(min_temperature - temperature):
            min_index = i
            min_temperature = temperature_list[i]
    return min_index + 1

if __name__ == '__main__':
    judge_temperature()
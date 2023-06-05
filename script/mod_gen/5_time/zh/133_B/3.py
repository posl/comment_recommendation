def get_distance(x, y):
    #计算两个点之间的距离
    distance = 0
    for i in range(len(x)):
        distance += (x[i] - y[i])**2
    return distance**0.5

if __name__ == '__main__':
    get_distance()
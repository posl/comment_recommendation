def calc_distance(n, x, y):
    #n: 顶点数
    #x: 顶点x
    #y: 顶点y
    #返回值: 距离列表
    # 0: 顶点x和顶点y之间的距离
    # 1: 顶点1和顶点2之间的距离
    # ...
    # n-1:顶点n-1和顶点n之间的距离
    distance_list = [0] * n
    for i in range(1, n):
        for j in range(i+1, n+1):
            distance_list[j-i] += 1
    return distance_list

if __name__ == '__main__':
    calc_distance()
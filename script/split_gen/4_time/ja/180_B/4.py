def cal_manhattan_distance(dimension, point_list):
    distance = 0
    for point in point_list:
        distance += abs(point)
    return distance

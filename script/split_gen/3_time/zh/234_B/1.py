def get_max_distance(points):
    max_distance = 0
    for i in range(len(points)):
        for j in range(i+1, len(points)):
            distance = get_distance(points[i], points[j])
            if distance > max_distance:
                max_distance = distance
    return max_distance

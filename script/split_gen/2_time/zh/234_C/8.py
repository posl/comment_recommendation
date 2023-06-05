def max_len(points):
    import math
    max_len = 0
    for i in range(len(points)):
        for j in range(i+1, len(points)):
            x = points[i][0] - points[j][0]
            y = points[i][1] - points[j][1]
            length = math.sqrt(x**2 + y**2)
            if max_len < length:
                max_len = length
    return max_len

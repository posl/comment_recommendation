def get_triangle_number(points):
    if len(points) < 3:
        return 0
    count = 0
    for i in range(len(points)):
        for j in range(i+1, len(points)):
            for k in range(j+1, len(points)):
                if get_area(points[i], points[j], points[k]) > 0:
                    count += 1
    return count

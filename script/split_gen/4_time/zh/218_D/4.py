def get_count_of_rectangles(points):
    count = 0
    for point in points:
        x, y = point
        for point2 in points:
            x2, y2 = point2
            if x2 > x and y2 > y:
                if (x, y2) in points and (x2, y) in points:
                    count += 1
    return count/2

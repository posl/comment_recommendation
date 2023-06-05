def is_line(points):
    if len(points) < 3:
        return False
    if points[0][0] == points[1][0] == points[2][0]:
        return True
    elif points[0][1] == points[1][1] == points[2][1]:
        return True
    elif points[0][0] == points[1][0] and points[1][0] == points[2][0]:
        return True
    elif points[0][1] == points[1][1] and points[1][1] == points[2][1]:
        return True
    elif points[0][0] == points[1][0] and points[1][0] == points[2][0]:
        return True
    elif points[0][1] == points[1][1] and points[1][1] == points[2][1]:
        return True
    else:
        k1 = (points[0][1] - points[1][1]) / (points[0][0] - points[1][0])
        k2 = (points[1][1] - points[2][1]) / (points[1][0] - points[2][0])
        if k1 == k2:
            return True
    return False

if __name__ == '__main__':
    is_line()
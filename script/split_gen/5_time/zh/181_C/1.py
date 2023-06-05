def is_line(points):
    if len(points) < 3:
        return False
    else:
        for i in range(len(points)):
            for j in range(i+1, len(points)):
                for k in range(j+1, len(points)):
                    if points[i][0] == points[j][0] == points[k][0] or points[i][1] == points[j][1] == points[k][1]:
                        return True
        return False

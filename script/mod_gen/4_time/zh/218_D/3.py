def get_rects(points):
    points = sorted(points)
    rects = []
    for i in range(len(points)):
        for j in range(i+1, len(points)):
            if points[i][0] == points[j][0] or points[i][1] == points[j][1]:
                continue
            if (points[i][0], points[j][1]) in points and (points[j][0], points[i][1]) in points:
                rects.append((points[i], points[j]))
    return rects

if __name__ == '__main__':
    get_rects()
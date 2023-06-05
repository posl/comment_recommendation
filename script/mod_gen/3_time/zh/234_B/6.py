def get_max_distance(points):
    max_distance = 0
    for i in range(len(points)):
        for j in range(i+1, len(points)):
            distance = ((points[i][0] - points[j][0])**2 + (points[i][1] - points[j][1])**2)**(1/2)
            if distance > max_distance:
                max_distance = distance
    return max_distance

if __name__ == '__main__':
    get_max_distance()
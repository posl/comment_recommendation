def max_length(points):
    max_length = 0
    for i in range(len(points) - 1):
        for j in range(i + 1, len(points)):
            length = (points[i][0] - points[j][0]) ** 2 + (points[i][1] - points[j][1]) ** 2
            if length > max_length:
                max_length = length
    return max_length ** 0.5

if __name__ == '__main__':
    max_length()
def get_max_len(points):
    max_len = 0
    for i in range(len(points)):
        for j in range(i+1, len(points)):
            x = points[i][0] - points[j][0]
            y = points[i][1] - points[j][1]
            d = x*x + y*y
            if d > max_len:
                max_len = d
    return max_len

if __name__ == '__main__':
    get_max_len()
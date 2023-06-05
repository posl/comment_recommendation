def max_len(points):
    max_len = 0
    for i in range(len(points)):
        for j in range(i+1, len(points)):
            len = points[i].length(points[j])
            if len > max_len:
                max_len = len
    return max_len

if __name__ == '__main__':
    max_len()
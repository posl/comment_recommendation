def max_len(N, points):
    max_len = 0
    for i in range(N):
        for j in range(i+1, N):
            x1 = points[i][0]
            y1 = points[i][1]
            x2 = points[j][0]
            y2 = points[j][1]
            len = ((x1-x2)**2 + (y1-y2)**2)**0.5
            if len > max_len:
                max_len = len
    return max_len

if __name__ == '__main__':
    max_len()
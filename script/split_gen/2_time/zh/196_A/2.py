def max_x_y(a,b,c,d):
    max_x_y = 0
    for i in range(a,b+1):
        for j in range(c,d+1):
            if i-j > max_x_y:
                max_x_y = i-j
    return max_x_y

def get_rect_num(x, y):
    rect_num = 0
    for i in range(len(x)):
        for j in range(i+1, len(x)):
            if x[i] == x[j] or y[i] == y[j]:
                continue
            if (x[i], y[j]) in point_set and (x[j], y[i]) in point_set:
                rect_num += 1
    return rect_num

if __name__ == '__main__':
    get_rect_num()
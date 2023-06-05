def get_max_value(w, v, x, l, r):
    # 从l到r中选出最大的x
    max_x = x[l-1]
    for i in range(l, r):
        if x[i] > max_x:
            max_x = x[i]
    # 从w中选出最大的x
    max_w = w[0]
    for i in range(1, len(w)):
        if w[i] > max_w:
            max_w = w[i]
    # 如果最大的x比最大的w大，说明可以把所有的w放入箱子
    if max_x > max_w:
        return sum(v)
    else:
        # 如果最大的x比最大的w小，说明不能把所有的w放入箱子
        # 从w中选出最大的x，然后把这个w放入箱子
        max_x_index = w.index(max_w)
        new_w = w.copy()
        new_w[max_x_index] = max_x
        return sum(new_w)

if __name__ == '__main__':
    get_max_value()
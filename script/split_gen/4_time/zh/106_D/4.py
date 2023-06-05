def train_num(train, start, end):
    num = 0
    for i in range(len(train)):
        if train[i][0] >= start and train[i][1] <= end:
            num += 1
    return num

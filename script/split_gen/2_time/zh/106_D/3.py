def get_num_of_train(start,end,train_list):
    num_of_train = 0
    for train in train_list:
        if train[0] >= start and train[1] <= end:
            num_of_train += 1
    return num_of_train

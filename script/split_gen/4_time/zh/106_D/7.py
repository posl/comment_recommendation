def get_train_num(p,q):
    train_num = 0
    for i in range(1,M+1):
        if L[i] >= p and R[i] <= q:
            train_num += 1
    return train_num

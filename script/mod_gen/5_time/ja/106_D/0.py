def count_train(l, r, trains):
    cnt = 0
    for train in trains:
        if l <= train[0] and train[1] <= r:
            cnt += 1
    return cnt

if __name__ == '__main__':
    count_train()
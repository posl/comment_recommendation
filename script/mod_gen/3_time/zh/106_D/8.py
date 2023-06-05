def count_trains(l,r,train):
    count = 0
    for i in range(len(train)):
        if train[i][0] >= l and train[i][1] <= r:
            count += 1
    return count

if __name__ == '__main__':
    count_trains()
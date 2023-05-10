def count_trains(start, end, trains):
    count = 0
    for train in trains:
        if train[0] >= start and train[1] <= end:
            count += 1
    return count

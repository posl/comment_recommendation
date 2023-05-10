def count_trains_within_section(trains, p, q):
    count = 0
    for train in trains:
        if p <= train[0] and train[1] <= q:
            count += 1
    return count

if __name__ == '__main__':
    count_trains_within_section()
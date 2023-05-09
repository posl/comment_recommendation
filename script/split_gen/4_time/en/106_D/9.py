def train_count(n, m, q, trains, queries):
    trains_count = []
    for query in queries:
        count = 0
        for train in trains:
            if query[0] <= train[0] and train[1] <= query[1]:
                count += 1
        trains_count.append(count)
    return trains_count

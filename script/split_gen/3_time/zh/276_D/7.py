def count_operation(a):
    count = 0
    while True:
        if all([x % 2 == 0 for x in a]):
            a = [x / 2 for x in a]
            count += 1
        elif all([x % 3 == 0 for x in a]):
            a = [x / 3 for x in a]
            count += 1
        elif all([x == a[0] for x in a]):
            return count
        else:
            return -1

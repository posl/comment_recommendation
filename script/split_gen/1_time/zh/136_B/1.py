def count_odd_digits(n):
    count = 0
    for i in range(1, n+1):
        if i < 10:
            if i % 2 != 0:
                count += 1
        else:
            if i % 2 != 0:
                count += 1
            else:
                if i % 10 != 0:
                    if i % 100 != 0:
                        if i % 1000 != 0:
                            if i % 10000 != 0:
                                if i % 100000 != 0:
                                    if i % 1000000 != 0:
                                        if i % 10000000 != 0:
                                            if i % 100000000 != 0:
                                                if i % 1000000000 != 0:
                                                    count += 1
    return count

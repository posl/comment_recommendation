def countop(a):
    count = 0
    for i in a:
        while i % 2 == 0:
            i /= 2
            count += 1
    return count

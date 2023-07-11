def count_odd(l):
    count = 0
    for i in range(len(l)):
        if l[i] % 2 == 1:
            count += 1
    return count

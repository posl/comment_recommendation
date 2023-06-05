def count_dec(num):
    count = 0
    for i in range(1, num+1):
        if '7' in str(i):
            count += 1
    return count

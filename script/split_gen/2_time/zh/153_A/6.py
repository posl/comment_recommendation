def get_num(n):
    count = 0
    for i in range(1,n+1):
        if i < 10:
            count += 1
            continue
        if i % 10 == int(str(i)[0]):
            count += 1
    return count

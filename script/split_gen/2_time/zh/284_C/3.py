def odd_number(num):
    count = 0
    for i in range(num):
        if num[i] % 2 == 1:
            count += 1
    return count

def count7(num):
    count = 0
    for i in range(1,num+1):
        if '7' not in str(i) and '7' not in oct(i):
            count += 1
    return count

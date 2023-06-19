def count753(num):
    count = 0
    for i in range(1, num+1):
        if '7' in str(i) and '5' in str(i) and '3' in str(i):
            count += 1
    return count

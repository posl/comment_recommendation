def count_comma(n):
    count = 0
    for i in range(1, len(str(n))+1):
        if i % 3 == 0:
            count += 1
    return count

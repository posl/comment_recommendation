def seven_count(n):
    count = 0
    for i in range(n+1):
        if str(i).count('7') + oct(i).count('7') == 0:
            count += 1
    return count

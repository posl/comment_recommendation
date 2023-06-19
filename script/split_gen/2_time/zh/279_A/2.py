def count_bottom(str):
    count = 0
    for i in range(len(str)):
        if str[i] == 'v':
            for j in range(i,len(str)):
                if str[j] == 'v':
                    count += 1
    return count

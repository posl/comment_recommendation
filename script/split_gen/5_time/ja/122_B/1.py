def count_acgt(str):
    count = 0
    max_count = 0
    for i in range(len(str)):
        if str[i] == "A" or str[i] == "C" or str[i] == "G" or str[i] == "T":
            count += 1
            if max_count < count:
                max_count = count
        else:
            count = 0
    return max_count

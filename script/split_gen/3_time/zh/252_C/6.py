def get_match_count(str1, str2):
    count = 0
    for i in range(10):
        if str1[i] == str2[i]:
            count += 1
    return count

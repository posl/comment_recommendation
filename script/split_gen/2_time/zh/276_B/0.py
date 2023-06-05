def last_index_of_a(s):
    index = -1
    for i in range(len(s)):
        if s[i] == 'a':
            index = i + 1
    return index

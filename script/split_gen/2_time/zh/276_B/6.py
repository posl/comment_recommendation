def get_index(s):
    index = -1
    for i in range(len(s)):
        if s[i] == 'a':
            index = i + 1
    return index

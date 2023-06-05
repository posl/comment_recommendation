def get_index(s):
    count = 0
    for i in range(len(s)):
        count += (26 ** (i + 1))
    return count

def count_bottoms(s):
    count = 0
    for i in range(len(s)):
        if s[i] == 'w':
            count += len(s) - i
    return count

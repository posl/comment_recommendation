def count_bottom(s):
    count = 0
    for i in range(len(s)):
        if s[i] == 'w':
            count += s[i+1:].count('v')
    return count

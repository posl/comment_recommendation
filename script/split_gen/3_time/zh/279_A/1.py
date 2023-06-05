def count_bottoms(s):
    count = 0
    for i in range(len(s)):
        if s[i] == 'v':
            for j in range(i+1, len(s)):
                if s[j] == 'v':
                    count += 1
    return count

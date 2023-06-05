def count_bottoms(s):
    count = 0
    for i in range(len(s)):
        if s[i] == 'v':
            for j in range(i, len(s)):
                if s[j] == 'v':
                    count += 1
                else:
                    break
    return count

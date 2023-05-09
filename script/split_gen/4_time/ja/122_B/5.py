def count_acgt(s):
    count = 0
    max_count = 0
    for i in range(len(s)):
        if s[i] == 'A' or s[i] == 'C' or s[i] == 'G' or s[i] == 'T':
            count += 1
            if max_count < count:
                max_count = count
        else:
            count = 0
    return max_count
s = input()
print(count_acgt(s))

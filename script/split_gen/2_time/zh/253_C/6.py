def find_min_max(s):
    min = s[0]
    max = s[0]
    for i in range(len(s)):
        if s[i] < min:
            min = s[i]
        if s[i] > max:
            max = s[i]
    return max - min

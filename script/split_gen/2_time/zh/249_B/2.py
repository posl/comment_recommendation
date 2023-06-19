def is_wonderful_string(s):
    s = sorted(s)
    for i in range(len(s)-1):
        if s[i] == s[i+1]:
            return 'No'
    if 'a' <= s[0] <= 'z' and 'A' <= s[len(s)-1] <= 'Z':
        return 'Yes'
    else:
        return 'No'

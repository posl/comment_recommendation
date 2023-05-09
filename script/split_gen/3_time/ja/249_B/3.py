def is_upper_and_lower(s):
    is_upper = False
    is_lower = False
    for i in range(len(s)):
        if s[i].isupper():
            is_upper = True
        if s[i].islower():
            is_lower = True
    return is_upper and is_lower

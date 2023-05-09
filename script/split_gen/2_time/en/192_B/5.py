def hard_to_read(s):
    for i in range(0, len(s), 2):
        if s[i].islower():
            continue
        else:
            return "No"
    for i in range(1, len(s), 2):
        if s[i].isupper():
            continue
        else:
            return "No"
    return "Yes"

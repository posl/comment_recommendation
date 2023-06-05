def is_easy(s):
    for i in range(0, len(s), 2):
        if s[i] == 'L':
            return False
    for i in range(1, len(s), 2):
        if s[i] == 'R':
            return False
    return True

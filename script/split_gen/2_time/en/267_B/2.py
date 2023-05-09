def is_split(s):
    if s[0] == '0':
        return False
    for i in range(1, 10):
        if s[i] == '1':
            if s[i-1] == '1':
                return True
            if s[i+1] == '1':
                return True
    return False
s = input()

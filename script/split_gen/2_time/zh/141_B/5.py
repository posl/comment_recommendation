def func(s):
    if len(s) % 2 == 1:
        return 'No'
    else:
        if s[0] == 'L' or s[len(s) - 1] == 'L':
            return 'No'
        else:
            for i in range(0, len(s), 2):
                if s[i] == 'L':
                    return 'No'
            for i in range(1, len(s), 2):
                if s[i] != 'L':
                    return 'No'
            return 'Yes'

def get_possible_passwords(s):
    possible_passwords = 1
    for i in range(10):
        if s[i] == 'o':
            possible_passwords *= 1
        elif s[i] == 'x':
            possible_passwords *= 0
        else:
            possible_passwords *= 10
    return possible_passwords

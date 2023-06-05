def is_ac():
    s = input()
    if s[0] == 'A' and 'C' in s[2:-1] and s[1:].islower():
        return 'AC'
    else:
        return 'WA'

def split_pin(s):
    if s[0] == '0':
        return 'No'
    if s[1] == '1':
        return 'No'
    if s[2] == '1':
        return 'No'
    if s[3] == '1':
        return 'No'
    if s[4] == '1':
        return 'No'
    if s[5] == '1':
        return 'No'
    if s[6] == '1':
        return 'No'
    if s[7] == '1':
        return 'No'
    if s[8] == '1':
        return 'No'
    if s[9] == '1':
        return 'No'
    return 'Yes'
s = input()
print(split_pin(s))

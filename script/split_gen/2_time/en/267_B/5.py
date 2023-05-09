def bowling_pins(s):
    if s[0] == '0':
        return 'No'
    if s[1:4] == '000' and s[4:7] == '000' and s[7:10] == '000':
        return 'No'
    if s[1:4] == '000' and s[4:7] == '000' and s[7:10] == '111':
        return 'No'
    if s[1:4] == '000' and s[4:7] == '111' and s[7:10] == '000':
        return 'No'
    if s[1:4] == '111' and s[4:7] == '000' and s[7:10] == '000':
        return 'No'
    if s[1:4] == '000' and s[4:7] == '111' and s[7:10] == '111':
        return 'No'
    if s[1:4] == '111' and s[4:7] == '000' and s[7:10] == '111':
        return 'No'
    if s[1:4] == '111' and s[4:7] == '111' and s[7:10] == '000':
        return 'No'
    if s[1:4] == '111' and s[4:7] == '111' and s[7:10] == '111':
        return 'No'
    return 'Yes'

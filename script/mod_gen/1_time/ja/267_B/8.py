def bowling_pins(s):
    if s[0] == '0':
        return 'No'
    for i in range(1, 10):
        if s[i] == '1' and '0' in s[i+1:]:
            return 'Yes'
    return 'No'

if __name__ == '__main__':
    bowling_pins()
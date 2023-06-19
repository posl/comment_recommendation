def split_pin(s):
    if s[0] == '0':
        return 'No'
    for i in range(1, 10):
        if s[i] == '0':
            if s[i - 1] == '1':
                return 'No'
    return 'Yes'

if __name__ == '__main__':
    split_pin()
def bowling_pins(s):
    if s[0] != '0':
        return 'No'
    for i in range(1, 10):
        if s[i] == '1':
            if s[i-1] == '1' or s[i+1] == '1':
                return 'Yes'
    return 'No'
s = input()
print(bowling_pins(s))

if __name__ == '__main__':
    bowling_pins()
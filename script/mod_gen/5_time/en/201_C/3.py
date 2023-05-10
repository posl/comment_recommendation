def check_pin(pin, s):
    for i in range(10):
        if s[i] == 'o':
            if str(i) not in pin:
                return False
        elif s[i] == 'x':
            if str(i) in pin:
                return False
    return True

if __name__ == '__main__':
    check_pin()
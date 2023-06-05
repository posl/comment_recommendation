def problem202_b():
    s = input()
    s = s[::-1]
    s = s.replace('6', 't')
    s = s.replace('9', '6')
    s = s.replace('t', '9')
    s = s.replace('0', 't')
    s = s.replace('1', '0')
    s = s.replace('t', '1')
    print(s)

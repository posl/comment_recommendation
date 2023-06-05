def problem124_c():
    s = input()
    s1 = s.replace('0', ' ')
    s2 = s1.split()
    s3 = s.replace('1', ' ')
    s4 = s3.split()
    if len(s2) > len(s4):
        print(len(s4))
    else:
        print(len(s2))

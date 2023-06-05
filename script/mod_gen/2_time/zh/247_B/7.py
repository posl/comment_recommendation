def problem247_a(s):
    # print(s)
    s = s.replace('1','2')
    s = s.replace('0','1')
    s = s.replace('2','0')
    print(s)
problem247_a('1011')
problem247_a('0000')
problem247_a('1111')

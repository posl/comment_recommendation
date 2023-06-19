def problem202_b():
    s=input()
    s=s[::-1]
    s=s.replace('0','a')
    s=s.replace('1','b')
    s=s.replace('6','1')
    s=s.replace('8','2')
    s=s.replace('9','6')
    s=s.replace('a','0')
    s=s.replace('b','1')
    print(s)
problem202_b()

def main():
    s = input()
    s = s[::-1]
    s = s.replace('0','t')
    s = s.replace('1','r')
    s = s.replace('6','y')
    s = s.replace('8','8')
    s = s.replace('9','6')
    s = s.replace('t','9')
    s = s.replace('r','1')
    s = s.replace('y','0')
    print(s)

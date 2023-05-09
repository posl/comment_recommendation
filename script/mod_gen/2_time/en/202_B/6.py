def rotate180(s):
    s = s[::-1]
    s = s.replace('0','2')
    s = s.replace('1','3')
    s = s.replace('2','0')
    s = s.replace('3','1')
    s = s.replace('6','4')
    s = s.replace('8','5')
    s = s.replace('9','6')
    s = s.replace('4','8')
    s = s.replace('5','9')
    s = s.replace('7','7')
    return s
s = input()
print(rotate180(s))

if __name__ == '__main__':
    rotate180()
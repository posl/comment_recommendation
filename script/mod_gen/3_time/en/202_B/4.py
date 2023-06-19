def rotate(s):
    s = s[::-1]
    s = s.replace('6','a')
    s = s.replace('9','6')
    s = s.replace('a','9')
    return s
s = input()
print(rotate(s))

def rotate_180(s):
    #print(s)
    s = s[::-1]
    s = s.replace("0","x")
    s = s.replace("1","y")
    s = s.replace("6","0")
    s = s.replace("8","8")
    s = s.replace("9","6")
    s = s.replace("x","9")
    s = s.replace("y","1")
    return s
s = input()
print(rotate_180(s))

if __name__ == '__main__':
    rotate_180()
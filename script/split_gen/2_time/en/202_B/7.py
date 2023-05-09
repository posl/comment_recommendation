def rotate_string(s):
    #reverse string
    s = s[::-1]
    #replace 6 with 9 and vice versa
    s = s.replace("6", "2")
    s = s.replace("9", "6")
    s = s.replace("2", "9")
    return s
s = input()
print(rotate_string(s))

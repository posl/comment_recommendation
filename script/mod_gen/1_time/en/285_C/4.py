def main():
    import string
    import math
    s = input()
    l = len(s)
    if l == 1:
        print(string.ascii_uppercase.index(s)+1)
    elif l == 2:
        print(26 + string.ascii_uppercase.index(s[1]) + 1)
    elif l == 3:
        print(26 + 26 + string.ascii_uppercase.index(s[2]) + 1)
    elif l == 4:
        print(26 + 26 + 26 + string.ascii_uppercase.index(s[3]) + 1)
    elif l == 5:
        print(26 + 26 + 26 + 26 + string.ascii_uppercase.index(s[4]) + 1)
    elif l == 6:
        print(26 + 26 + 26 + 26 + 26 + string.ascii_uppercase.index(s[5]) + 1)
    elif l == 7:
        print(26 + 26 + 26 + 26 + 26 + 26 + string.ascii_uppercase.index(s[6]) + 1)
    elif l == 8:
        print(26 + 26 + 26 + 26 + 26 + 26 + 26 + string.ascii_uppercase.index(s[7]) + 1)
    elif l == 9:
        print(26 + 26 + 26 + 26 + 26 + 26 + 26 + 26 + string.ascii_uppercase.index(s[8]) + 1)
    elif l == 10:
        print(26 + 26 + 26 + 26 + 26 + 26 + 26 + 26 + 26 + string.ascii_uppercase.index(s[9]) + 1)
    elif l == 11:
        print(26 + 26 + 26 + 26 + 26 + 26 + 26 + 26 + 26

if __name__ == '__main__':
    main()
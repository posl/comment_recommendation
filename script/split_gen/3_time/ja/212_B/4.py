def main():
    s = input()
    if s[0] == s[1] == s[2] == s[3]:
        print('Weak')
    elif int(s[0]) == (int(s[1]) - 1) % 10 and int(s[1]) == (int(s[2]) - 1) % 10 and int(s[2]) == (int(s[3]) - 1) % 10:
        print('Weak')
    else:
        print('Strong')

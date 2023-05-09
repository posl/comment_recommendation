def main():
    s = input()
    if s[0] == s[1] == s[2] == s[3]:
        print('Weak')
    else:
        for i in range(3):
            if s[i] == '9':
                if s[i+1] != '0':
                    print('Strong')
                    exit()
            else:
                if int(s[i])+1 != int(s[i+1]):
                    print('Strong')
                    exit()
        print('Weak')

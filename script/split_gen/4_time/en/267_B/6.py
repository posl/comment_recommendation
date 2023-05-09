def main():
    s = input()
    if s[0] == '0':
        print('No')
    else:
        if s[1] == '0' or s[2] == '0':
            print('No')
        else:
            if s[3] == '0' or s[4] == '0' or s[5] == '0':
                print('No')
            else:
                if s[6] == '0' or s[7] == '0' or s[8] == '0' or s[9] == '0':
                    print('No')
                else:
                    print('Yes')

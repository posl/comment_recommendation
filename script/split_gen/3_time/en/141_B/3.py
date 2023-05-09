def main():
    s = input()
    if (s[0] == 'R' or s[0] == 'U' or s[0] == 'D') and (s[1] == 'L' or s[1] == 'U' or s[1] == 'D'):
        for i in range(2,len(s)):
            if i % 2 == 0:
                if s[i] == 'R' or s[i] == 'U' or s[i] == 'D':
                    pass
                else:
                    print('No')
                    exit()
            else:
                if s[i] == 'L' or s[i] == 'U' or s[i] == 'D':
                    pass
                else:
                    print('No')
                    exit()
        print('Yes')
    else:
        print('No')

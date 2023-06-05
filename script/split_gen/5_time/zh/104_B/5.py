def main():
    s = input()
    if s[0] == 'A' and s[2:-1].count('C') == 1:
        for i in range(len(s)):
            if i == 0:
                continue
            elif i == 1:
                if s[i] != 'C':
                    print('WA')
                    exit()
            elif i == len(s) - 1:
                if s[i].isupper():
                    print('WA')
                    exit()
            else:
                if s[i].isupper():
                    print('WA')
                    exit()
        print('AC')
    else:
        print('WA')

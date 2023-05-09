def main():
    s = input()
    if s[0] == 'A' and s[2:-1].count('C') == 1 and s[1].islower() and s[-1].islower():
        for i in range(2, len(s)):
            if s[i] != 'C' and not s[i].islower():
                print('WA')
                return
        print('AC')
    else:
        print('WA')

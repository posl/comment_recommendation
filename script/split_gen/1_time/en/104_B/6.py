def main():
    s = input()
    if s[0] == 'A' and s[2:-1].count('C') == 1:
        if s[1].islower() and s[-1].islower() and s[2:-1].islower():
            print('AC')
            return
    print('WA')

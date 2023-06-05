def main():
    s = input()
    if s[0] == 'A' and 'C' in s[2:-1] and s.count('C') == 1 and s[1:].islower():
        print('AC')
    else:
        print('WA')

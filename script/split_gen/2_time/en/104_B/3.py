def main():
    s = input()
    if s[0] == 'A' and s[2:-1].count('C') == 1 and s[1:].lower() == s[1:]:
        print('AC')
    else:
        print('WA')

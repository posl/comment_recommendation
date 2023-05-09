def main():
    s = input()
    if s[0] != 'A':
        print('WA')
        return
    if s[2:-1].count('C') != 1:
        print('WA')
        return
    if s[1:].lower() != s[1:]:
        print('WA')
        return
    if s[2:].lower() != s[2:]:
        print('WA')
        return
    print('AC')

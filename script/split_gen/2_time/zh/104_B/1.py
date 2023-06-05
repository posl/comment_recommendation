def main():
    s = input()
    if s[0] != 'A':
        print('WA')
        return
    if s[2:-1].count('C') != 1:
        print('WA')
        return
    if len(s) < 4:
        print('WA')
        return
    for i in range(len(s)):
        if i == 0 or i == 2 or i == len(s) - 1:
            continue
        if s[i].isupper():
            print('WA')
            return
    print('AC')

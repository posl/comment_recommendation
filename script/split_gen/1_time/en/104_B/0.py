def main():
    s = input()
    if s[0] != 'A':
        print('WA')
        return
    if s[2:-1].count('C') != 1:
        print('WA')
        return
    for i in range(1, len(s)):
        if i == 1:
            continue
        if s[i] == 'C':
            continue
        if s[i].isupper():
            print('WA')
            return
    print('AC')

def main():
    s = input()
    if s[0] != 'A':
        print('WA')
        return
    if s[2:-1].count('C') != 1:
        print('WA')
        return
    for i in s:
        if i == 'A' or i == 'C':
            continue
        if i.isupper():
            print('WA')
            return
    print('AC')

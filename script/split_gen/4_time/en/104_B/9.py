def main():
    s = input()
    if s[0] == 'A' and s[2:-1].count('C') == 1:
        for i in range(len(s)):
            if s[i].isupper():
                if i == 0 or i == 2 or i == len(s) - 1:
                    continue
                else:
                    print('WA')
                    return
        print('AC')
    else:
        print('WA')

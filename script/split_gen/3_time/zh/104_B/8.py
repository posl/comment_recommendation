def main():
    s=input()
    if s[0]=='A' and s[2:-1].count('C')==1:
        for i in s[1:]:
            if i.isupper():
                print('WA')
                break
        else:
            print('AC')
    else:
        print('WA')

def main():
    s = input()
    if s.islower():
        print('No')
    elif s.isupper():
        print('No')
    elif len(s) == 1:
        print('No')
    elif len(s) == 2:
        if s[0] == s[1]:
            print('No')
        else:
            print('Yes')
    else:
        if s[0] == s[1]:
            print('No')
        elif s[0] == s[-1]:
            print('No')
        elif s[1] == s[-1]:
            print('No')
        else:
            print('Yes')

def solve():
    s = input()
    if s[::2].islower() and s[1::2].isupper():
        print('Yes')
    else:
        print('No')

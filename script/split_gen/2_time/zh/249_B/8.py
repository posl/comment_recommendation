def main():
    s = input()
    if s[0].isupper() and s[1].islower() and s[2:].islower():
        print('Yes')
    else:
        print('No')

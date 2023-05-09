def main():
    s = input()
    if s[0::2].count('R') + s[0::2].count('U') + s[0::2].count('D') == len(s[0::2]) and s[1::2].count('L') + s[1::2].count('U') + s[1::2].count('D') == len(s[1::2]):
        print('Yes')
    else:
        print('No')

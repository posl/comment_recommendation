def main():
    s = input()
    s1 = s[::2]
    s2 = s[1::2]
    if s1.count('L') + s2.count('R') + s1.count('U') + s2.count('D') == 0:
        print('Yes')
    else:
        print('No')

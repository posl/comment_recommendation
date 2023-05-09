def main():
    s1 = input()
    s2 = input()
    if s1[0] == s1[1] == s2[0] == s2[1] == '#':
        print('Yes')
    elif s1[0] == s1[1] == s2[0] == s2[1] == '.':
        print('Yes')
    else:
        print('No')

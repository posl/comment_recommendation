def main():
    s1 = input()
    s2 = input()
    if s1[1] == '#' and s2[1] == '#' or s1[1] == '#' and s2[0] == '#' or s1[0] == '#' and s2[1] == '#' or s1[0] == '#' and s2[0] == '#':
        print('Yes')
    else:
        print('No')

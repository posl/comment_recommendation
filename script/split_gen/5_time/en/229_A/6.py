def main():
    S1 = input()
    S2 = input()
    if S1[1] == '#' and S2[1] == '#' or S1[1] == '.' and S2[1] == '.':
        print('No')
    else:
        print('Yes')

def main():
    s = input()
    if s[0] != '1':
        print('No')
    else:
        s = s[1:]
        if s.count('1') == 1:
            print('No')
        else:
            print('Yes')

def main():
    s = input()
    if s[0] == '0':
        print('No')
        return
    if s[1:10].count('1') == 0:
        print('No')
        return
    if s[1:10].count('0') == 0:
        print('No')
        return
    print('Yes')

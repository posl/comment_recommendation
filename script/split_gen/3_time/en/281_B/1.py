def main():
    s = input()
    if len(s) != 10:
        print('No')
        return
    if s[0].isupper() and s[1:7].isdigit() and int(s[1:7]) >= 100000 and int(s[1:7]) <= 999999 and s[7].isupper():
        print('Yes')
    else:
        print('No')

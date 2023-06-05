def main():
    s = input()
    if s.count(s[0]) == 2 and s.count(s[1]) == 2:
        print('Yes')
    else:
        print('No')

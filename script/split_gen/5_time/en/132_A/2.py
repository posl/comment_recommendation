def main():
    s = input()
    if len(set(s)) == 2:
        if s.count(s[0]) == 2:
            print('Yes')
        else:
            print('No')
    else:
        print('No')

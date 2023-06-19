def main():
    s = input()
    if len(s) == 4 and s.isupper():
        if len(set(s)) == 2:
            print('Yes')
        else:
            print('No')

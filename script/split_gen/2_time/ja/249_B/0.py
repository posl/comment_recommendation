def main():
    s = input()
    if s.islower() or s.isupper():
        print('No')
    elif len(s) != len(set(s)):
        print('No')
    else:
        print('Yes')

def main():
    s = input()
    if 'A' in s and 'a' in s and len(s) == len(set(s)):
        print('Yes')
    else:
        print('No')

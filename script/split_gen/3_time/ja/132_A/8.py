def main():
    s = input()
    if len(s) == len(set(s)):
        print('Yes')
    else:
        print('No')

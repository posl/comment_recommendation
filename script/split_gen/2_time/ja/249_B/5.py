def main():
    s = input()
    if 'A' in s and 'a' in s:
        if len(set(s)) == len(s):
            print('Yes')
            return
    print('No')

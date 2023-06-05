def main():
    s = input()
    for i in range(0, len(s), 2):
        if s[i].isupper():
            print('No')
            return
    for i in range(1, len(s), 2):
        if s[i].islower():
            print('No')
            return
    print('Yes')

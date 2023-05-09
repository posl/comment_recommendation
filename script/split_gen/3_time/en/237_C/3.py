def main():
    s = input()
    for i in range(len(s)):
        if s[i] != s[-i-1]:
            print('No')
            exit()
    print('Yes')

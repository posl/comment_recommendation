def main():
    s = input()
    n = len(s)
    for i in range(n):
        if s[i] != s[-i-1]:
            print('No')
            exit()
    for i in range(n//2):
        if s[i] != s[-i-1]:
            print('No')
            exit()
    print('Yes')

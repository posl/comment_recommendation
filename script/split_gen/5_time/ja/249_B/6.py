def main():
    s = input()
    s = sorted(s)
    for i in range(len(s)-1):
        if s[i] == s[i+1]:
            print('No')
            exit()
    if ord(s[0]) >= ord('a') and ord(s[-1]) <= ord('z'):
        print('Yes')
    else:
        print('No')

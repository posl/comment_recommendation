def main():
    s = input()
    for i in range(len(s)):
        if (i+1) % 2 == 1:
            if s[i] == 'L':
                print('No')
                return
        else:
            if s[i] == 'R':
                print('No')
                return
    print('Yes')

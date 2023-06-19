def main():
    s = input()
    for i in range(len(s)):
        if (i + 1) % 2 == 1:
            if s[i] not in ['R', 'U', 'D']:
                print('No')
                return
        else:
            if s[i] not in ['L', 'U', 'D']:
                print('No')
                return
    print('Yes')

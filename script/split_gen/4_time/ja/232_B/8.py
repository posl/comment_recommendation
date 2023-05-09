def main():
    s = input()
    t = input()
    for i in range(len(s)):
        if s[i] == t[i]:
            continue
        else:
            if s[i] == 'z':
                if t[i] == 'a':
                    continue
                else:
                    print('No')
                    exit()
            elif s[i] == 'a':
                if t[i] == 'z':
                    continue
                else:
                    print('No')
                    exit()
            else:
                if s[i] < t[i]:
                    print('Yes')
                    exit()
                else:
                    print('No')
                    exit()
    print('Yes')
    exit()

def main():
    s = input()
    if s[0] == 'R' or s[0] == 'U' or s[0] == 'D':
        for i in range(1,len(s)):
            if i % 2 == 0:
                if s[i] == 'L' or s[i] == 'U' or s[i] == 'D':
                    continue
                else:
                    print('No')
                    break
            else:
                if s[i] == 'R' or s[i] == 'U' or s[i] == 'D':
                    continue
                else:
                    print('No')
                    break
        else:
            print('Yes')
    else:
        print('No')

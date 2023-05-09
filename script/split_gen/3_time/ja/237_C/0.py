def main():
    s = input()
    for i in range(len(s)):
        if s[i] != s[len(s)-1-i]:
            if s[i] == 'a' or s[len(s)-1-i] == 'a':
                if i == len(s)-1-i:
                    print('Yes')
                    return
                if s[i+1] == s[len(s)-2-i] or s[i] == s[len(s)-2-i]:
                    print('Yes')
                    return
            else:
                print('No')
                return
    print('Yes')

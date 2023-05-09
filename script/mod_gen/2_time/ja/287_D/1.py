def match(s,t):
    for i in range(len(t)):
        if s[i] != t[i] and s[i] != '?' and t[i] != '?':
            return False
    return True
s = input()
t = input()
for i in range(len(t)+1):
    if match(s[:i]+s[len(s)-len(t)+i:],t):
        print('Yes')
    else:
        print('No')

if __name__ == '__main__':
    match()
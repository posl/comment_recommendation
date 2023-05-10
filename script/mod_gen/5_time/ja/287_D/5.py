def match(s,t):
    for i in range(len(t)):
        if s[i] == '?':
            continue
        if s[i] != t[i]:
            return False
    return True
s = input()
t = input()
n = len(s)
m = len(t)
for i in range(n-m+1):
    if match(s[i:i+m],t):
        print('Yes')
    else:
        print('No')

if __name__ == '__main__':
    match()
def check(s):
    if s[0] == 'H' or s[0] == 'D' or s[0] == 'C' or s[0] == 'S':
        if s[1] == 'A' or s[1] == '2' or s[1] == '3' or s[1] == '4' or s[1] == '5' or s[1] == '6' or s[1] == '7' or s[1] == '8' or s[1] == '9' or s[1] == 'T' or s[1] == 'J' or s[1] == 'Q' or s[1] == 'K':
            return True
        else:
            return False
    else:
        return False
n = int(input())
s = []
for i in range(n):
    s.append(input())
for i in range(n):
    for j in range(i+1, n):
        if s[i] == s[j]:
            print('No')
            exit()
for i in range(n):
    if not check(s[i]):
        print('No')
        exit()
print('Yes')

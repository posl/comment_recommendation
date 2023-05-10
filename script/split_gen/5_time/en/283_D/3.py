def check(s):
    if len(s) == 0:
        return True
    if len(s) == 1:
        return False
    if len(s) == 2:
        return False
    if s[0] == '(' and s[-1] == ')':
        return check(s[1:-1])
    else:
        return False
S = input()
a = [0]*len(S)
b = [0]*len(S)
c = [0]*len(S)
d = [0]*len(S)
for i in range(len(S)):
    if S[i] == '(':
        a[i] = 1
    if S[i] == ')':
        b[i] = 1
    if S[i] >= 'a' and S[i] <= 'z':
        c[i] = 1
    if S[i] >= 'A' and S[i] <= 'Z':
        d[i] = 1

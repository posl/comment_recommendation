def isGood(s):
    if len(s) == 0:
        return True
    if s[0] == '(':
        return False
    if s[-1] == ')':
        return False
    if len(s) == 1:
        return True
    if len(s) == 2:
        if s[0] != s[1]:
            return True
        else:
            return False
    if s[0] == s[-1]:
        return False
    return isGood(s[1:-1])
S = input()
T = ''
for i in range(len(S)):
    if S[i] == '(':
        T += '('
    elif S[i] == ')':
        T = T[:-1]
    else:
        T += S[i]
    if not isGood(T):
        print('No')
        exit()

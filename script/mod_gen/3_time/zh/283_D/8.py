def isGoodString(s):
    if len(s) == 0:
        return True
    if len(s) == 1:
        return False
    if len(s) == 2:
        return s == '()'
    if s[0] == ')' or s[-1] == '(':
        return False
    if s[0] == '(' and s[-1] == ')':
        return isGoodString(s[1:-1])
    return isGoodString(s[1:-1])

if __name__ == '__main__':
    isGoodString()
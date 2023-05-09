def isGoodString(s):
    if len(s) == 0:
        return True
    if s[0] == ')':
        return False
    if s[-1] == '(':
        return False
    if s.count('(') != s.count(')'):
        return False
    if s.count('(') == 0:
        return True
    if s.count('(') == 1 and s.count(')') == 1:
        return True
    if s.count('(') == 2 and s.count(')') == 2:
        return True
    if s.count('(') == 3 and s.count(')') == 3:
        return True
    return False

if __name__ == '__main__':
    isGoodString()
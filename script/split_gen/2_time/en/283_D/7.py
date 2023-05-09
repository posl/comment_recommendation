def check_good_string(s):
    #print(s)
    if len(s) == 0:
        return True
    if len(s) == 1:
        return False
    if s[0] == ')':
        return False
    if s[-1] == '(':
        return False
    if s[0] == '(' and s[-1] == ')':
        return check_good_string(s[1:-1])
    if s[0] == '(':
        return check_good_string(s[1:])
    if s[-1] == ')':
        return check_good_string(s[:-1])
    return check_good_string(s[1:-1])

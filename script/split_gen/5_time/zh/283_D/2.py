def check(s):
    while '()' in s:
        s = s.replace('()','')
    if s == '':
        return True
    else:
        return False

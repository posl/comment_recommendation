def check_year_month_format(s):
    if s[0] == '0':
        return False
    if s[0] == '1':
        if s[1] in ['0','1','2']:
            return True
    if s[0] == '2':
        if s[1] in ['0','1','2','3']:
            return True
    return False

def replace(s):
    if s.startswith('na'):
        return 'nya' + s[2:]
    else:
        return s

def replace_na(s):
    #print(s)
    if 'na' in s:
        s = s.replace('na', 'nya')
        s = replace_na(s)
    return s

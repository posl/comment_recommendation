def replace_na(s):
    #print(s)
    if 'na' in s:
        s = s.replace('na', 'nya')
        s = replace_na(s)
    return s

if __name__ == '__main__':
    replace_na()
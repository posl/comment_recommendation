def replace_na(s):
    while 'na' in s:
        s = s.replace('na','nya')
    return s

if __name__ == '__main__':
    replace_na()
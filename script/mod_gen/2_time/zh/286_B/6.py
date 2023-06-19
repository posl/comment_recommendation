def replace_na(s):
    if 'na' not in s:
        return s
    return replace_na(s.replace('na', 'nya', 1))

if __name__ == '__main__':
    replace_na()
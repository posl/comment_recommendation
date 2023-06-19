def replace_na(s):
    if 'na' not in s:
        return s
    return replace_na(s.replace('na', 'nya', 1))

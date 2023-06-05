def replace_na_with_nya(s):
    new_s = s.replace('na', 'nya')
    if new_s == s:
        return new_s
    else:
        return replace_na_with_nya(new_s)

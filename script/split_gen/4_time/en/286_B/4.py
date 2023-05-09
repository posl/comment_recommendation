def replace_na(s):
    if 'na' in s:
        return replace_na(s.replace('na', 'nya'))
    else:
        return s

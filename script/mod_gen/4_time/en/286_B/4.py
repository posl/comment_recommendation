def replace_na(s):
    if 'na' in s:
        return replace_na(s.replace('na', 'nya'))
    else:
        return s

if __name__ == '__main__':
    replace_na()
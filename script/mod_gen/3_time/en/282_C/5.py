def replace_comma(s):
    s = list(s)
    for i in range(len(s)):
        if s[i] == ',':
            s[i] = '.'
    return ''.join(s)

if __name__ == '__main__':
    replace_comma()
def replace_comma(s):
    s = list(s)
    cnt = 0
    for i in range(len(s)):
        if s[i] == '"':
            cnt += 1
        elif s[i] == ',' and cnt % 2 == 1:
            s[i] = '.'
    return ''.join(s)

if __name__ == '__main__':
    replace_comma()
def replace(s):
    s = list(s)
    s[0] = '"'
    s[-1] = '"'
    for i in range(1, len(s)-1):
        if s[i] == '"':
            if s[i-1] == ',':
                s[i-1] = '.'
            if s[i+1] == ',':
                s[i+1] = '.'
    return "".join(s)

if __name__ == '__main__':
    replace()
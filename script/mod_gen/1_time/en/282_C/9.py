def replaceCommas(s):
    s = s[0:len(s)-1]
    s = s.replace(',"', '.')
    s = s + '"'
    return s

if __name__ == '__main__':
    replaceCommas()
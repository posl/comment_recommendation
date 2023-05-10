def alternate_string(s, t):
    result = ''
    for i in range(len(s)):
        result += s[i]
        result += t[i]
    return result

if __name__ == '__main__':
    alternate_string()